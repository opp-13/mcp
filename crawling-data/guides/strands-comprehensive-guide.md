# Strands Agents 종합 가이드

## 개요
Strands Agents는 AWS에서 개발한 오픈소스 AI 에이전트 SDK로, 모델 중심 접근법을 통해 몇 줄의 코드만으로 강력한 AI 에이전트를 구축할 수 있습니다.

## 핵심 특징

### 1. 경량 및 유연성
- 간단한 에이전트 루프로 즉시 작동
- 완전히 커스터마이징 가능한 구조
- 복잡한 설정 없이 빠른 시작

### 2. 모델 독립성
지원하는 모델 제공자:
- Amazon Bedrock (기본)
- Anthropic Claude
- OpenAI GPT
- LiteLLM
- Llama
- Ollama
- Writer
- 사용자 정의 제공자

### 3. 고급 기능
- 멀티 에이전트 시스템
- 자율 에이전트
- 스트리밍 지원
- 내장 MCP (Model Context Protocol) 지원

## 설치 및 시작

```bash
# 기본 설치
pip install strands-agents

# 도구 포함 설치
pip install strands-agents strands-agents-tools
```

### 기본 에이전트 생성
```python
from strands import Agent

# 기본 에이전트 생성
agent = Agent()

# 질문하기
response = agent("Tell me about agentic AI")
print(response)
```

## 멀티 에이전트 협업

### 에이전트를 도구로 사용하는 패턴
```python
from strands import Agent
from strands.tools import tool

@tool
def calendar_agent(query: str) -> str:
    """캘린더 관련 작업을 처리하는 에이전트"""
    calendar_agent = Agent(tools=[list_appointments, create_appointment])
    return calendar_agent(query)

@tool
def search_agent(query: str) -> str:
    """웹 검색을 수행하는 에이전트"""
    search_agent = Agent(tools=[web_search])
    return search_agent(query)

# 마스터 에이전트가 하위 에이전트들을 조율
master_agent = Agent(
    tools=[calendar_agent, search_agent],
    system_prompt="당신은 개인 비서입니다. 필요에 따라 적절한 에이전트를 호출하세요."
)

# 복합 요청 처리
response = master_agent("내일 회의 일정을 확인하고, 회의 주제에 대해 검색해주세요")
```

## 도구 시스템

### 1. 내장 도구
```python
from strands_tools import (
    current_time,      # 현재 시간
    python_repl,       # Python 코드 실행
    shell_command,     # 셸 명령 실행
    file_editor,       # 파일 편집
    web_search,        # 웹 검색
    retrieve           # Bedrock 지식 기반 검색
)

agent = Agent(tools=[current_time, python_repl, file_editor])
```

### 2. 사용자 정의 도구
```python
from strands.tools import tool

@tool
def calculate_tax(income: float, tax_rate: float) -> float:
    """소득세를 계산합니다."""
    return income * tax_rate

@tool
def get_weather(city: str) -> str:
    """특정 도시의 날씨를 조회합니다."""
    # API 호출 로직
    return f"{city}의 현재 날씨는 맑음입니다."

agent = Agent(tools=[calculate_tax, get_weather])
```

### 3. MCP 서버 통합
```python
from strands.mcp import MCPClient

# MCP 서버 연결
mcp_client = MCPClient("perplexity-mcp-server")
tools = mcp_client.list_tools()

agent = Agent(tools=tools)
```

## AWS 서비스 통합

### Bedrock 설정
```python
from strands.models import BedrockModel

model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20241022-v2:0",
    region="us-west-2"
)

agent = Agent(model=model)
```

### AWS 도구 사용
```python
from strands_tools import use_aws, retrieve

# AWS 서비스 호출
agent = Agent(tools=[
    use_aws,     # Boto3를 통한 AWS 서비스 호출
    retrieve     # Bedrock 지식 기반 검색
])

response = agent("S3 버킷 목록을 조회해주세요")
```

## 실제 사용 사례

### 1. 개인 비서 시스템
```python
# 캘린더, 검색, 코드 어시스턴트를 통합한 개인 비서
class PersonalAssistant:
    def __init__(self):
        self.calendar_agent = Agent(tools=[calendar_tools])
        self.search_agent = Agent(tools=[search_tools])
        self.code_agent = Agent(tools=[code_tools])
        
        self.master = Agent(tools=[
            self.calendar_agent,
            self.search_agent,
            self.code_agent
        ])
    
    def process(self, request):
        return self.master(request)
```

### 2. 고객 서비스 시스템
```python
# 문의 분류, 라우팅, 추적을 담당하는 멀티 에이전트 시스템
class CustomerServiceSystem:
    def __init__(self):
        self.classifier = Agent(tools=[classify_inquiry])
        self.router = Agent(tools=[route_to_specialist])
        self.tracker = Agent(tools=[track_resolution])
        
        self.orchestrator = Agent(tools=[
            self.classifier,
            self.router,
            self.tracker
        ])
```

### 3. 데이터 분석 에이전트
```python
# 데이터 수집, 분석, 시각화를 수행하는 에이전트
data_agent = Agent(tools=[
    python_repl,
    file_editor,
    web_search,
    use_aws  # S3, Athena 등 AWS 데이터 서비스 활용
])

response = data_agent("""
S3에서 판매 데이터를 가져와서 
월별 트렌드를 분석하고 
시각화 차트를 생성해주세요
""")
```

## 배포 옵션

### 1. AWS Lambda
```python
import json
from strands import Agent

def lambda_handler(event, context):
    agent = Agent()
    response = agent(event['query'])
    
    return {
        'statusCode': 200,
        'body': json.dumps({'response': response})
    }
```

### 2. FastAPI 서버
```python
from fastapi import FastAPI
from strands import Agent

app = FastAPI()
agent = Agent()

@app.post("/chat")
async def chat(query: str):
    response = agent(query)
    return {"response": response}
```

### 3. ECS/Fargate
```dockerfile
FROM python:3.11-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "agent_server.py"]
```

## 모니터링 및 관찰성

### 추적 설정
```python
from strands import Agent

agent = Agent(
    trace_attributes={
        "environment": "production",
        "version": "1.0.0",
        "user_id": "user123"
    }
)

# OpenTelemetry와 통합하여 Datadog, Arize 등에서 모니터링
```

## 베스트 프랙티스

### 1. 시스템 프롬프트 최적화
```python
system_prompt = """
당신은 전문적인 고객 서비스 에이전트입니다.
- 항상 정중하고 도움이 되는 톤을 유지하세요
- 불확실한 정보는 확인 후 답변하세요
- 필요시 적절한 도구를 사용하세요
"""

agent = Agent(system_prompt=system_prompt)
```

### 2. 에러 처리
```python
try:
    response = agent(user_query)
except Exception as e:
    # 에러 로깅 및 대체 응답
    logger.error(f"Agent error: {e}")
    response = "죄송합니다. 일시적인 오류가 발생했습니다."
```

### 3. 성능 최적화
```python
# 모델 설정 최적화
model = BedrockModel(
    model_id="anthropic.claude-3-5-haiku-20241022-v1:0",  # 빠른 응답용
    max_tokens=1000,
    temperature=0.1
)

agent = Agent(model=model)
```

## 주요 저장소

- **SDK**: https://github.com/strands-agents/sdk-python
- **도구**: https://github.com/strands-agents/tools  
- **샘플**: https://github.com/strands-agents/samples
- **문서**: https://github.com/strands-agents/docs
- **MCP 서버**: https://github.com/strands-agents/mcp-server

## 커뮤니티 및 지원

- 공식 문서: https://strandsagents.com
- GitHub 이슈: 각 저장소의 Issues 탭
- 기여 가이드: CONTRIBUTING.md 참조
- 라이선스: Apache License 2.0
