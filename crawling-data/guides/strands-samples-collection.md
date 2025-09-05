# Strands Agents 샘플 코드 모음

## 1. 기본 에이전트 패턴

### Hello World 에이전트
```python
from strands import Agent

# 가장 간단한 에이전트
agent = Agent()
response = agent("Hello, world!")
print(response)
```

### 시스템 프롬프트가 있는 에이전트
```python
from strands import Agent

agent = Agent(
    system_prompt="당신은 친근한 AI 어시스턴트입니다. 항상 도움이 되는 답변을 제공하세요."
)

response = agent("파이썬에 대해 설명해주세요")
```

## 2. 도구 사용 패턴

### 내장 도구 사용
```python
from strands import Agent
from strands_tools import current_time, python_repl

agent = Agent(tools=[current_time, python_repl])

# 현재 시간 확인
response = agent("지금 몇 시인가요?")

# 계산 수행
response = agent("2의 10제곱을 계산해주세요")
```

### 사용자 정의 도구
```python
from strands import Agent
from strands.tools import tool

@tool
def get_stock_price(symbol: str) -> str:
    """주식 가격을 조회합니다."""
    # 실제로는 API 호출
    prices = {"AAPL": "$150.00", "GOOGL": "$2800.00", "TSLA": "$800.00"}
    return f"{symbol} 주식 가격: {prices.get(symbol, '정보 없음')}"

@tool
def calculate_compound_interest(principal: float, rate: float, years: int) -> str:
    """복리 이자를 계산합니다."""
    amount = principal * (1 + rate/100) ** years
    return f"원금 ${principal:,.2f}, 연이율 {rate}%, {years}년 후: ${amount:,.2f}"

agent = Agent(tools=[get_stock_price, calculate_compound_interest])

response = agent("AAPL 주식 가격을 확인하고, 1000달러를 5% 이율로 10년간 투자하면 얼마가 될까요?")
```

## 3. 멀티 에이전트 패턴

### 에이전트를 도구로 사용
```python
from strands import Agent
from strands.tools import tool
from strands_tools import web_search, current_time

@tool
def research_agent(topic: str) -> str:
    """특정 주제에 대해 연구하는 에이전트"""
    agent = Agent(
        tools=[web_search],
        system_prompt="당신은 연구 전문가입니다. 정확하고 신뢰할 수 있는 정보를 제공하세요."
    )
    return agent(f"{topic}에 대해 최신 정보를 조사해주세요")

@tool
def analysis_agent(data: str) -> str:
    """데이터를 분석하는 에이전트"""
    agent = Agent(
        system_prompt="당신은 데이터 분석 전문가입니다. 핵심 인사이트를 도출하세요."
    )
    return agent(f"다음 데이터를 분석해주세요: {data}")

# 마스터 에이전트
coordinator = Agent(
    tools=[research_agent, analysis_agent],
    system_prompt="당신은 프로젝트 코디네이터입니다. 적절한 전문가에게 작업을 할당하세요."
)

response = coordinator("AI 시장 동향을 조사하고 분석해주세요")
```

### 스웜 패턴 (여러 에이전트 협업)
```python
from strands import Agent
from strands.tools import tool

class CustomerServiceSwarm:
    def __init__(self):
        # 문의 분류 에이전트
        self.classifier = Agent(
            system_prompt="고객 문의를 기술지원, 결제, 일반문의로 분류하세요."
        )
        
        # 기술 지원 에이전트
        self.tech_support = Agent(
            system_prompt="기술적 문제를 해결하는 전문가입니다."
        )
        
        # 결제 지원 에이전트
        self.billing_support = Agent(
            system_prompt="결제 및 요금 관련 문의를 처리하는 전문가입니다."
        )
        
        # 일반 지원 에이전트
        self.general_support = Agent(
            system_prompt="일반적인 고객 문의를 처리하는 친근한 어시스턴트입니다."
        )
    
    def process_inquiry(self, inquiry: str) -> str:
        # 1단계: 문의 분류
        classification = self.classifier(f"다음 문의를 분류해주세요: {inquiry}")
        
        # 2단계: 적절한 에이전트에게 라우팅
        if "기술" in classification or "오류" in classification:
            return self.tech_support(inquiry)
        elif "결제" in classification or "요금" in classification:
            return self.billing_support(inquiry)
        else:
            return self.general_support(inquiry)

# 사용 예시
swarm = CustomerServiceSwarm()
response = swarm.process_inquiry("로그인이 안 되는데 도와주세요")
```

## 4. AWS 통합 패턴

### Bedrock 모델 사용
```python
from strands import Agent
from strands.models import BedrockModel

# Claude 모델 사용
model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20241022-v2:0",
    region="us-west-2",
    max_tokens=2000,
    temperature=0.7
)

agent = Agent(model=model)
```

### AWS 서비스 통합
```python
from strands import Agent
from strands_tools import use_aws, retrieve

# AWS 서비스를 사용하는 에이전트
aws_agent = Agent(
    tools=[use_aws, retrieve],
    system_prompt="AWS 서비스를 활용하여 클라우드 관리 작업을 수행하세요."
)

# S3 버킷 목록 조회
response = aws_agent("현재 계정의 S3 버킷 목록을 보여주세요")

# EC2 인스턴스 상태 확인
response = aws_agent("실행 중인 EC2 인스턴스들의 상태를 확인해주세요")
```

### Bedrock 지식 기반 활용
```python
from strands import Agent
from strands_tools import retrieve

kb_agent = Agent(
    tools=[retrieve],
    system_prompt="지식 기반을 활용하여 정확한 정보를 제공하세요."
)

response = kb_agent("회사 정책에 따른 휴가 신청 절차를 알려주세요")
```

## 5. MCP 서버 통합 패턴

### Perplexity MCP 서버 사용
```python
from strands import Agent
from strands.mcp import MCPClient

# MCP 서버 연결
perplexity_client = MCPClient("perplexity-mcp-server")
tools = perplexity_client.list_tools()

search_agent = Agent(
    tools=tools,
    system_prompt="웹 검색을 통해 최신 정보를 제공하세요."
)

response = search_agent("2024년 AI 기술 동향에 대해 검색해주세요")
```

### 여러 MCP 서버 통합
```python
from strands import Agent
from strands.mcp import MCPClient

# 여러 MCP 서버 연결
weather_client = MCPClient("weather-mcp-server")
news_client = MCPClient("news-mcp-server")
finance_client = MCPClient("finance-mcp-server")

all_tools = []
all_tools.extend(weather_client.list_tools())
all_tools.extend(news_client.list_tools())
all_tools.extend(finance_client.list_tools())

comprehensive_agent = Agent(
    tools=all_tools,
    system_prompt="날씨, 뉴스, 금융 정보를 종합하여 도움을 제공하세요."
)
```

## 6. 실제 애플리케이션 패턴

### 개인 비서 에이전트
```python
from strands import Agent
from strands.tools import tool
from strands_tools import current_time, web_search, python_repl

@tool
def manage_calendar(action: str, details: str = "") -> str:
    """캘린더 관리 (조회, 생성, 수정, 삭제)"""
    # 실제로는 캘린더 API 연동
    if action == "list":
        return "오늘 일정: 10:00 팀 미팅, 14:00 고객 미팅, 16:00 프로젝트 리뷰"
    elif action == "create":
        return f"새 일정이 생성되었습니다: {details}"
    return "캘린더 작업이 완료되었습니다."

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """이메일 발송"""
    # 실제로는 이메일 API 연동
    return f"{to}에게 '{subject}' 제목으로 이메일을 발송했습니다."

personal_assistant = Agent(
    tools=[current_time, web_search, python_repl, manage_calendar, send_email],
    system_prompt="""
    당신은 개인 비서입니다. 다음 작업을 수행할 수 있습니다:
    - 일정 관리 (조회, 생성, 수정)
    - 웹 검색 및 정보 조회
    - 계산 및 데이터 분석
    - 이메일 발송
    - 현재 시간 확인
    
    항상 정중하고 효율적으로 작업을 수행하세요.
    """
)

# 사용 예시
response = personal_assistant("""
내일 오전 10시에 마케팅 팀과 미팅을 잡고,
최신 AI 트렌드에 대해 검색한 후
팀장에게 요약 이메일을 보내주세요.
""")
```

### 코드 어시스턴트
```python
from strands import Agent
from strands_tools import python_repl, file_editor, shell_command

code_assistant = Agent(
    tools=[python_repl, file_editor, shell_command],
    system_prompt="""
    당신은 코드 어시스턴트입니다. 다음 작업을 수행할 수 있습니다:
    - Python 코드 작성 및 실행
    - 파일 읽기, 쓰기, 편집
    - 셸 명령 실행
    - 디버깅 및 테스트
    
    코드는 항상 깔끔하고 주석이 포함되도록 작성하세요.
    """
)

response = code_assistant("""
간단한 웹 스크래퍼를 만들어주세요.
requests와 BeautifulSoup을 사용해서
뉴스 사이트에서 헤드라인을 가져오는 코드를 작성하고 실행해보세요.
""")
```

### 데이터 분석 에이전트
```python
from strands import Agent
from strands_tools import python_repl, file_editor
from strands.tools import tool

@tool
def load_data_from_s3(bucket: str, key: str) -> str:
    """S3에서 데이터를 로드합니다."""
    # 실제로는 boto3를 사용하여 S3에서 데이터 로드
    return f"S3://{bucket}/{key}에서 데이터를 성공적으로 로드했습니다."

@tool
def save_chart_to_s3(chart_path: str, bucket: str, key: str) -> str:
    """차트를 S3에 저장합니다."""
    # 실제로는 boto3를 사용하여 S3에 업로드
    return f"차트가 S3://{bucket}/{key}에 저장되었습니다."

data_analyst = Agent(
    tools=[python_repl, file_editor, load_data_from_s3, save_chart_to_s3],
    system_prompt="""
    당신은 데이터 분석 전문가입니다. 다음 작업을 수행할 수 있습니다:
    - 데이터 로드 및 전처리
    - 통계 분석 및 시각화
    - 머신러닝 모델 구축
    - 결과 해석 및 인사이트 도출
    
    pandas, numpy, matplotlib, seaborn 등의 라이브러리를 활용하세요.
    """
)

response = data_analyst("""
sales-data.csv 파일을 분석해서
월별 매출 트렌드를 시각화하고
향후 3개월 매출을 예측해주세요.
""")
```

## 7. 배포 패턴

### Lambda 함수로 배포
```python
import json
from strands import Agent
from strands_tools import current_time

# Lambda 핸들러
def lambda_handler(event, context):
    agent = Agent(
        tools=[current_time],
        system_prompt="간결하고 정확한 답변을 제공하세요."
    )
    
    try:
        query = event.get('query', '')
        response = agent(query)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'response': response,
                'success': True
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'success': False
            })
        }
```

### FastAPI 서버로 배포
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strands import Agent
from strands_tools import current_time, web_search

app = FastAPI(title="Strands Agent API")

# 요청 모델
class ChatRequest(BaseModel):
    query: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    response: str
    session_id: str

# 에이전트 초기화
agent = Agent(
    tools=[current_time, web_search],
    system_prompt="도움이 되는 AI 어시스턴트입니다."
)

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = agent(request.query)
        return ChatResponse(
            response=response,
            session_id=request.session_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 8. 고급 패턴

### 상태 관리가 있는 에이전트
```python
from strands import Agent
from strands.tools import tool

class StatefulAgent:
    def __init__(self):
        self.conversation_history = []
        self.user_preferences = {}
        
        @tool
        def remember_preference(key: str, value: str) -> str:
            """사용자 선호도를 기억합니다."""
            self.user_preferences[key] = value
            return f"{key} 선호도가 {value}로 저장되었습니다."
        
        @tool
        def get_preference(key: str) -> str:
            """저장된 사용자 선호도를 조회합니다."""
            return self.user_preferences.get(key, "설정된 선호도가 없습니다.")
        
        self.agent = Agent(
            tools=[remember_preference, get_preference],
            system_prompt="사용자의 선호도를 기억하고 개인화된 서비스를 제공하세요."
        )
    
    def chat(self, query: str) -> str:
        # 대화 기록에 추가
        self.conversation_history.append({"user": query})
        
        # 컨텍스트에 이전 대화 포함
        context = f"이전 대화: {self.conversation_history[-3:]}\n현재 질문: {query}"
        response = self.agent(context)
        
        # 응답 기록에 추가
        self.conversation_history.append({"assistant": response})
        
        return response

# 사용 예시
stateful_agent = StatefulAgent()
response1 = stateful_agent.chat("저는 커피를 좋아해요")
response2 = stateful_agent.chat("음료 추천해주세요")  # 커피 선호도를 기억함
```

### 에러 복구가 있는 에이전트
```python
from strands import Agent
from strands.tools import tool
import logging

class ResilientAgent:
    def __init__(self):
        self.retry_count = 0
        self.max_retries = 3
        
        @tool
        def safe_calculation(expression: str) -> str:
            """안전한 계산을 수행합니다."""
            try:
                # 안전한 eval 대신 실제로는 더 안전한 파서 사용
                result = eval(expression)
                return f"계산 결과: {result}"
            except Exception as e:
                return f"계산 오류: {str(e)}"
        
        self.agent = Agent(
            tools=[safe_calculation],
            system_prompt="오류가 발생하면 다른 방법을 시도하세요."
        )
    
    def chat_with_retry(self, query: str) -> str:
        for attempt in range(self.max_retries):
            try:
                response = self.agent(query)
                self.retry_count = 0  # 성공 시 리셋
                return response
            except Exception as e:
                logging.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == self.max_retries - 1:
                    return "죄송합니다. 일시적인 오류로 인해 요청을 처리할 수 없습니다."
                self.retry_count += 1
        
        return "최대 재시도 횟수를 초과했습니다."

# 사용 예시
resilient_agent = ResilientAgent()
response = resilient_agent.chat_with_retry("복잡한 계산을 해주세요")
```

이러한 패턴들을 조합하여 더욱 복잡하고 강력한 AI 에이전트 시스템을 구축할 수 있습니다.
