# Strands Agents API 레퍼런스

## 핵심 클래스

### Agent 클래스
```python
from strands import Agent

class Agent:
    def __init__(
        self,
        model: Optional[Model] = None,
        tools: Optional[List[Tool]] = None,
        system_prompt: Optional[str] = None,
        trace_attributes: Optional[Dict[str, Any]] = None,
        max_iterations: int = 10,
        **kwargs
    ):
        """
        AI 에이전트를 생성합니다.
        
        Args:
            model: 사용할 언어 모델 (기본값: BedrockModel)
            tools: 에이전트가 사용할 도구 목록
            system_prompt: 에이전트의 역할과 행동을 정의하는 시스템 프롬프트
            trace_attributes: 추적을 위한 메타데이터
            max_iterations: 최대 반복 횟수
        """
    
    def __call__(self, query: str) -> str:
        """
        에이전트에게 질문하고 응답을 받습니다.
        
        Args:
            query: 사용자 질문
            
        Returns:
            에이전트의 응답
        """
    
    def stream(self, query: str) -> Iterator[str]:
        """
        스트리밍 방식으로 응답을 받습니다.
        
        Args:
            query: 사용자 질문
            
        Yields:
            응답의 각 청크
        """
```

## 모델 클래스

### BedrockModel
```python
from strands.models import BedrockModel

class BedrockModel:
    def __init__(
        self,
        model_id: str = "anthropic.claude-3-5-sonnet-20241022-v2:0",
        region: str = "us-west-2",
        max_tokens: int = 2000,
        temperature: float = 0.7,
        top_p: float = 0.9,
        **kwargs
    ):
        """
        Amazon Bedrock 모델을 설정합니다.
        
        Args:
            model_id: Bedrock 모델 ID
            region: AWS 리전
            max_tokens: 최대 토큰 수
            temperature: 창의성 조절 (0.0-1.0)
            top_p: 토큰 선택 확률 임계값
        """

# 지원되는 Bedrock 모델들
BEDROCK_MODELS = {
    "claude-3-5-sonnet": "anthropic.claude-3-5-sonnet-20241022-v2:0",
    "claude-3-5-haiku": "anthropic.claude-3-5-haiku-20241022-v1:0", 
    "claude-3-opus": "anthropic.claude-3-opus-20240229-v1:0",
    "llama-3-1-70b": "meta.llama3-1-70b-instruct-v1:0",
    "llama-3-1-8b": "meta.llama3-1-8b-instruct-v1:0"
}
```

### AnthropicModel
```python
from strands.models import AnthropicModel

class AnthropicModel:
    def __init__(
        self,
        model_id: str = "claude-3-5-sonnet-20241022",
        api_key: Optional[str] = None,
        max_tokens: int = 2000,
        temperature: float = 0.7,
        **kwargs
    ):
        """
        Anthropic Claude 모델을 설정합니다.
        
        Args:
            model_id: Claude 모델 ID
            api_key: Anthropic API 키 (환경변수 ANTHROPIC_API_KEY 사용 가능)
            max_tokens: 최대 토큰 수
            temperature: 창의성 조절
        """
```

### OpenAIModel
```python
from strands.models import OpenAIModel

class OpenAIModel:
    def __init__(
        self,
        model_id: str = "gpt-4o",
        api_key: Optional[str] = None,
        max_tokens: int = 2000,
        temperature: float = 0.7,
        **kwargs
    ):
        """
        OpenAI GPT 모델을 설정합니다.
        
        Args:
            model_id: GPT 모델 ID
            api_key: OpenAI API 키 (환경변수 OPENAI_API_KEY 사용 가능)
            max_tokens: 최대 토큰 수
            temperature: 창의성 조절
        """
```

## 도구 시스템

### @tool 데코레이터
```python
from strands.tools import tool

@tool
def function_name(param1: type, param2: type = default) -> return_type:
    """
    도구의 설명을 여기에 작성합니다.
    이 설명은 모델이 도구를 언제 사용할지 결정하는 데 사용됩니다.
    
    Args:
        param1: 첫 번째 매개변수 설명
        param2: 두 번째 매개변수 설명 (선택사항)
        
    Returns:
        반환값 설명
    """
    # 도구 로직 구현
    return result

# 사용 예시
@tool
def get_weather(city: str, units: str = "celsius") -> str:
    """지정된 도시의 현재 날씨를 조회합니다."""
    # API 호출 로직
    return f"{city}의 현재 날씨: 맑음, 25°C"
```

### 내장 도구들

#### strands_tools 패키지
```python
from strands_tools import (
    # 시간 관련
    current_time,           # 현재 시간 조회
    
    # 코드 실행
    python_repl,           # Python 코드 실행
    shell_command,         # 셸 명령 실행
    
    # 파일 관리
    file_editor,           # 파일 읽기/쓰기/편집
    
    # 웹 관련
    web_search,            # 웹 검색
    
    # AWS 관련
    use_aws,               # AWS 서비스 호출
    retrieve,              # Bedrock 지식 기반 검색
    
    # 유틸리티
    journal,               # 작업 로그 관리
)

# 도구 사용 예시
agent = Agent(tools=[current_time, python_repl, web_search])
```

#### 개별 도구 설명

**current_time**
```python
# 현재 시간을 조회합니다
# 반환: ISO 8601 형식의 현재 시간
```

**python_repl**
```python
# Python 코드를 실행합니다
# 매개변수: code (str) - 실행할 Python 코드
# 반환: 실행 결과 또는 오류 메시지
```

**shell_command**
```python
# 셸 명령을 실행합니다
# 매개변수: command (str) - 실행할 셸 명령
# 반환: 명령 실행 결과
```

**file_editor**
```python
# 파일을 읽기, 쓰기, 편집합니다
# 매개변수: 
#   - action (str): "read", "write", "append", "edit"
#   - path (str): 파일 경로
#   - content (str, optional): 쓸 내용
# 반환: 파일 내용 또는 작업 결과
```

**web_search**
```python
# 웹 검색을 수행합니다
# 매개변수: query (str) - 검색 쿼리
# 반환: 검색 결과 요약
```

**use_aws**
```python
# AWS 서비스를 호출합니다
# 매개변수:
#   - service (str): AWS 서비스 이름 (예: "s3", "ec2")
#   - operation (str): 작업 이름 (예: "list_buckets")
#   - parameters (dict, optional): 작업 매개변수
# 반환: AWS API 호출 결과
```

**retrieve**
```python
# Bedrock 지식 기반에서 정보를 검색합니다
# 매개변수:
#   - query (str): 검색 쿼리
#   - knowledge_base_id (str): 지식 기반 ID
# 반환: 검색된 정보
```

## MCP (Model Context Protocol) 통합

### MCPClient 클래스
```python
from strands.mcp import MCPClient

class MCPClient:
    def __init__(
        self,
        server_name: str,
        transport: str = "stdio",
        **kwargs
    ):
        """
        MCP 서버에 연결합니다.
        
        Args:
            server_name: MCP 서버 이름
            transport: 전송 방식 ("stdio", "http", "sse")
        """
    
    def list_tools(self) -> List[Tool]:
        """MCP 서버가 제공하는 도구 목록을 가져옵니다."""
    
    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        """특정 도구를 호출합니다."""

# 사용 예시
mcp_client = MCPClient("perplexity-mcp-server")
tools = mcp_client.list_tools()
agent = Agent(tools=tools)
```

## 멀티 에이전트 패턴

### 에이전트 스웜
```python
from strands.swarm import Swarm, SwarmAgent

class SwarmAgent:
    def __init__(
        self,
        name: str,
        agent: Agent,
        handoff_conditions: Optional[List[str]] = None
    ):
        """
        스웜 에이전트를 정의합니다.
        
        Args:
            name: 에이전트 이름
            agent: Strands Agent 인스턴스
            handoff_conditions: 다른 에이전트로 넘길 조건들
        """

class Swarm:
    def __init__(self, agents: List[SwarmAgent]):
        """
        에이전트 스웜을 생성합니다.
        
        Args:
            agents: 스웜에 참여할 에이전트들
        """
    
    def run(self, query: str, initial_agent: str) -> str:
        """
        스웜을 실행합니다.
        
        Args:
            query: 초기 쿼리
            initial_agent: 시작할 에이전트 이름
            
        Returns:
            최종 결과
        """
```

## 관찰성 및 추적

### 추적 설정
```python
from strands import Agent

# 추적 속성 설정
agent = Agent(
    trace_attributes={
        "environment": "production",
        "version": "1.0.0",
        "user_id": "user123",
        "session_id": "session456"
    }
)

# OpenTelemetry 통합
import opentelemetry
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# 추적 데이터를 외부 시스템으로 전송
exporter = OTLPSpanExporter(endpoint="https://your-tracing-endpoint")
```

### 로깅 설정
```python
import logging

# Strands 로깅 설정
logging.getLogger("strands").setLevel(logging.INFO)

# 커스텀 로거
logger = logging.getLogger(__name__)

@tool
def logged_function(param: str) -> str:
    """로깅이 포함된 도구 함수"""
    logger.info(f"Function called with param: {param}")
    result = f"Processed: {param}"
    logger.info(f"Function result: {result}")
    return result
```

## 에러 처리

### 예외 클래스들
```python
from strands.exceptions import (
    StrandsError,           # 기본 Strands 예외
    ModelError,             # 모델 관련 오류
    ToolError,              # 도구 실행 오류
    MCPError,               # MCP 관련 오류
    ValidationError         # 입력 검증 오류
)

# 에러 처리 예시
try:
    response = agent(query)
except ModelError as e:
    logger.error(f"Model error: {e}")
    response = "모델 오류가 발생했습니다."
except ToolError as e:
    logger.error(f"Tool error: {e}")
    response = "도구 실행 중 오류가 발생했습니다."
except StrandsError as e:
    logger.error(f"Strands error: {e}")
    response = "시스템 오류가 발생했습니다."
```

## 설정 및 환경변수

### 환경변수 목록
```bash
# AWS 관련
AWS_REGION=us-west-2
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_key

# OpenAI
OPENAI_API_KEY=your_openai_key

# Strands 설정
STRANDS_LOG_LEVEL=INFO
STRANDS_MAX_ITERATIONS=10
STRANDS_TIMEOUT=30

# MCP 서버 설정
MCP_SERVER_TIMEOUT=10
MCP_SERVER_RETRIES=3
```

### 설정 파일
```python
# strands_config.py
from strands.config import Config

config = Config(
    default_model="bedrock",
    max_iterations=10,
    timeout=30,
    log_level="INFO",
    trace_enabled=True
)

# 에이전트에서 설정 사용
agent = Agent(config=config)
```

## 유틸리티 함수들

### 헬퍼 함수들
```python
from strands.utils import (
    validate_tools,         # 도구 유효성 검사
    format_response,        # 응답 포맷팅
    parse_tool_call,        # 도구 호출 파싱
    sanitize_input,         # 입력 정제
    measure_performance     # 성능 측정
)

# 사용 예시
@measure_performance
def expensive_operation():
    # 시간이 오래 걸리는 작업
    pass

# 도구 유효성 검사
valid_tools = validate_tools([tool1, tool2, tool3])
```

## 배치 처리

### 배치 에이전트
```python
from strands.batch import BatchAgent

class BatchAgent:
    def __init__(self, agent: Agent, batch_size: int = 10):
        """
        배치 처리를 위한 에이전트
        
        Args:
            agent: 기본 에이전트
            batch_size: 배치 크기
        """
    
    def process_batch(self, queries: List[str]) -> List[str]:
        """
        여러 쿼리를 배치로 처리합니다.
        
        Args:
            queries: 처리할 쿼리 목록
            
        Returns:
            응답 목록
        """

# 사용 예시
batch_agent = BatchAgent(agent, batch_size=5)
responses = batch_agent.process_batch([
    "질문 1",
    "질문 2", 
    "질문 3"
])
```

이 API 레퍼런스를 통해 Strands Agents의 모든 주요 기능을 활용할 수 있습니다.
