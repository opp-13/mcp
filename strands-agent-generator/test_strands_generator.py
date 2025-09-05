#!/usr/bin/env python3
"""Strands Agent 생성기 테스트"""

import json
from datetime import datetime
from typing import Any, Dict, List, Optional


def analyze_requirements(requirements: str) -> Dict[str, Any]:
    """요구사항을 분석하여 적절한 패턴을 결정합니다."""
    req_lower = requirements.lower()
    
    analysis = {
        "agent_type": "basic",
        "aws_services": [],
        "tools_needed": [],
        "deployment": "lambda",
        "complexity": "simple"
    }
    
    # 에이전트 타입 결정
    if any(word in req_lower for word in ["여러", "다중", "협업", "팀", "분업"]):
        analysis["agent_type"] = "multi_agent"
    elif any(word in req_lower for word in ["대화", "채팅", "상담", "문답"]):
        analysis["agent_type"] = "conversational"
    
    # AWS 서비스 감지
    aws_services = {
        "s3": ["s3", "파일", "저장", "업로드", "다운로드"],
        "dynamodb": ["dynamodb", "데이터베이스", "db", "저장", "조회"],
        "bedrock": ["bedrock", "ai", "모델", "생성", "추론"],
        "lambda": ["lambda", "서버리스", "함수"],
    }
    
    for service, keywords in aws_services.items():
        if any(keyword in req_lower for keyword in keywords):
            analysis["aws_services"].append(service)
    
    # 기본 서비스 추가
    if not analysis["aws_services"]:
        analysis["aws_services"] = ["bedrock"]
    
    # 도구 필요성 분석
    if any(word in req_lower for word in ["계산", "수학", "코드"]):
        analysis["tools_needed"].append("python_repl")
    if any(word in req_lower for word in ["검색", "찾기", "조회"]):
        analysis["tools_needed"].append("web_search")
    
    return analysis


def generate_basic_agent(requirements: str, analysis: Dict[str, Any]) -> str:
    """기본 에이전트 코드를 생성합니다."""
    
    aws_services = analysis["aws_services"]
    tools_needed = analysis["tools_needed"]
    
    # 코드 템플릿 생성
    code = f'''"""
{requirements}를 위한 Strands Agent

자동 생성된 코드입니다.
생성 시간: {datetime.now().isoformat()}
"""

from strands import Agent
from strands.models import BedrockModel
from strands.tools import tool
import boto3

# AWS 클라이언트 초기화
{f"s3_client = boto3.client('s3')" if "s3" in aws_services else ""}
{f"dynamodb = boto3.resource('dynamodb')" if "dynamodb" in aws_services else ""}

@tool
def process_request(request: str) -> str:
    """사용자 요청을 처리합니다."""
    return f"요청 '{{request}}'를 처리했습니다."

# 에이전트 설정
model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20241022-v2:0",
    region="us-west-2",
    max_tokens=2000,
    temperature=0.7
)

agent = Agent(
    model=model,
    tools=[process_request],
    system_prompt="""
당신은 {requirements}를 위한 전문 AI 어시스턴트입니다.

사용 가능한 AWS 서비스: {', '.join(aws_services)}

항상 도움이 되고 정확한 정보를 제공하며, 필요시 적절한 도구를 사용하세요.
"""
)

def main():
    """메인 실행 함수"""
    try:
        print("🤖 Strands Agent가 시작되었습니다!")
        print(f"목적: {requirements}")
        print(f"사용 가능한 AWS 서비스: {', '.join(aws_services)}")
        
        # 테스트 실행
        response = agent("안녕하세요! 어떻게 도와드릴까요?")
        print(f"응답: {{response}}")
        
        return response
    except Exception as e:
        print(f"오류 발생: {{e}}")
        return None

if __name__ == "__main__":
    main()
'''
    
    return code


def test_generator():
    """생성기 테스트"""
    
    test_cases = [
        "고객 주문을 처리하고 S3에 저장하는 에이전트",
        "여러 에이전트가 협업하여 데이터를 분석하는 시스템",
        "간단한 챗봇 에이전트",
        "파일을 업로드하고 DynamoDB에 메타데이터를 저장하는 에이전트"
    ]
    
    for i, requirements in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"테스트 {i}: {requirements}")
        print('='*60)
        
        # 요구사항 분석
        analysis = analyze_requirements(requirements)
        print(f"분석 결과: {json.dumps(analysis, indent=2, ensure_ascii=False)}")
        
        # 코드 생성
        generated_code = generate_basic_agent(requirements, analysis)
        print(f"\n생성된 코드 길이: {len(generated_code)} 문자")
        print("코드 미리보기:")
        print(generated_code[:500] + "..." if len(generated_code) > 500 else generated_code)


if __name__ == "__main__":
    test_generator()
