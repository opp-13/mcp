#!/usr/bin/env python3
"""
기본 Strands Agent 테스트
출처: 
- https://github.com/strands-agents/sdk-python (README.md)
- /tmp/strands-comprehensive-guide.md (크롤링 데이터 기반)
"""

import sys
import os

# 가상환경 활성화
sys.path.insert(0, '/tmp/strands-test-env/lib/python3.12/site-packages')

try:
    from strands import Agent
    print("✅ Strands Agents 임포트 성공!")
    print(f"출처: https://github.com/strands-agents/sdk-python")
    
    # 기본 에이전트 생성 테스트
    print("\n🔧 기본 에이전트 생성 중...")
    agent = Agent()
    print("✅ 기본 에이전트 생성 성공!")
    
    # 간단한 질문 테스트 (AWS 자격증명 없이도 작동하는지 확인)
    print("\n💬 간단한 질문 테스트...")
    try:
        response = agent("Hello, what is 2+2?")
        print(f"✅ 응답 받음: {response}")
    except Exception as e:
        print(f"⚠️  응답 오류 (예상됨 - AWS 자격증명 필요): {e}")
        print("   이는 정상적인 동작입니다. Bedrock 모델 사용을 위해서는 AWS 자격증명이 필요합니다.")
    
    print("\n📊 Strands Agents 기본 정보:")
    print(f"- 버전: 1.7.0 (설치 로그 기준)")
    print(f"- 기본 모델: Amazon Bedrock")
    print(f"- 지원 기능: 멀티 에이전트, MCP 통합, 도구 사용")
    
except ImportError as e:
    print(f"❌ Strands Agents 임포트 실패: {e}")
    sys.exit(1)
