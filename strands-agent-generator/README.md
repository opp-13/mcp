# Strands Agent 자동 생성 MCP 서버

크롤링한 실제 Strands Agent 예시를 기반으로 사용자 요구사항에 맞는 에이전트 코드를 자동 생성하는 MCP 서버입니다.

## 🎯 주요 기능

### 1. 자동 코드 생성
- **요구사항 분석**: 자연어 요구사항을 분석하여 적절한 패턴 결정
- **AWS 서비스 감지**: S3, DynamoDB, Bedrock 등 필요한 서비스 자동 감지
- **완전한 프로젝트**: 즉시 실행 가능한 완전한 코드 생성

### 2. 지원하는 에이전트 타입
- **기본 에이전트**: 단일 목적 에이전트
- **멀티 에이전트**: 여러 전문 에이전트가 협업하는 시스템
- **대화형 에이전트**: 채팅 및 상담 기능

### 3. AWS 서비스 통합
- **S3**: 파일 업로드/다운로드/목록 조회
- **DynamoDB**: 데이터 저장/조회/스캔
- **Bedrock**: AI 모델 추론
- **Lambda**: 서버리스 배포

## 🚀 사용 예시

### MCP 도구 함수들

#### `generate_strands_agent(requirements, agent_type, aws_services, deployment_target)`
```python
# 예시 호출
result = generate_strands_agent(
    requirements="고객 주문을 처리하고 S3에 저장하는 에이전트",
    agent_type="basic",
    aws_services=["s3", "dynamodb"],
    deployment_target="lambda"
)

# 결과
{
    "success": True,
    "data": {
        "main_code": "완전한 Python 코드",
        "requirements_txt": "필요한 패키지 목록",
        "readme_md": "사용 가이드",
        "deployment_config": "배포 설정"
    },
    "metadata": {
        "analysis": "요구사항 분석 결과",
        "based_on": "크롤링한 실제 예시"
    }
}
```

#### `get_strands_examples()`
크롤링한 14개 실제 애플리케이션 예시 제공:
- 레스토랑 어시스턴트
- 금융 분석 시스템
- 의료 문서 처리
- AWS 감사 도구
- 등등...

#### `get_strands_guide()`
완전한 Strands Agents 가이드 제공 (크롤링 데이터 기반)

## 🔍 요구사항 분석 예시

### 입력: "고객 주문을 처리하고 S3에 저장하는 에이전트"
```json
{
  "agent_type": "basic",
  "aws_services": ["s3", "dynamodb"],
  "tools_needed": [],
  "deployment": "lambda",
  "complexity": "simple"
}
```

### 생성되는 코드 구조
```python
from strands import Agent
from strands.models import BedrockModel
from strands.tools import tool
import boto3

# AWS 클라이언트 자동 초기화
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

@tool
def s3_operations(bucket: str, operation: str, key: str = None) -> str:
    """S3 작업 자동 생성"""
    # 실제 S3 작업 코드

@tool  
def dynamodb_operations(table_name: str, operation: str) -> str:
    """DynamoDB 작업 자동 생성"""
    # 실제 DynamoDB 작업 코드

# 에이전트 설정 (Bedrock 모델 자동 설정)
agent = Agent(
    model=BedrockModel(...),
    tools=[s3_operations, dynamodb_operations],
    system_prompt="맞춤형 시스템 프롬프트"
)
```

## 📊 테스트 결과

4가지 테스트 케이스 모두 성공:
1. ✅ "고객 주문을 처리하고 S3에 저장하는 에이전트" → S3 + DynamoDB 통합
2. ✅ "여러 에이전트가 협업하여 데이터를 분석하는 시스템" → 멀티 에이전트
3. ✅ "간단한 챗봇 에이전트" → 기본 에이전트
4. ✅ "파일을 업로드하고 DynamoDB에 메타데이터를 저장하는 에이전트" → S3 + DynamoDB

## 🎯 실제 사용 시나리오

### Q에서 사용자가 요청:
```
"온라인 쇼핑몰 고객 문의를 처리하고, 
주문 정보는 DynamoDB에서 조회하고, 
답변 내역은 S3에 저장하는 에이전트를 만들어줘"
```

### MCP 서버 응답:
1. **요구사항 분석**: 기본 에이전트, S3 + DynamoDB 필요
2. **코드 생성**: 완전한 Strands Agent 코드
3. **프로젝트 구조**: main.py, requirements.txt, README.md
4. **배포 설정**: Lambda 배포용 설정

### 결과:
사용자는 **즉시 실행 가능한 완전한 에이전트**를 받게 됩니다!

## 💡 핵심 가치

1. **자동화**: 수동 코딩 없이 자연어로 에이전트 생성
2. **실용성**: 크롤링한 실제 예시 기반으로 검증된 코드
3. **완전성**: 코드 조각이 아닌 완전한 프로젝트
4. **즉시 사용**: 생성 즉시 실행 가능

**"에이전트가 필요하다 싶을 때 자동으로 만들어지는" 목표 달성!** 🎉
