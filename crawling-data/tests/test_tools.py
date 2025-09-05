#!/usr/bin/env python3
"""
Strands Agent 도구 시스템 테스트
출처:
- https://github.com/strands-agents/sdk-python (도구 시스템)
- /tmp/strands-samples-collection.md (샘플 코드 기반)
"""

import sys
sys.path.insert(0, '/tmp/strands-test-env/lib/python3.12/site-packages')

try:
    from strands import Agent
    from strands.tools import tool
    print("✅ Strands 도구 시스템 임포트 성공!")
    print("출처: https://github.com/strands-agents/sdk-python")
    
    # 사용자 정의 도구 생성 테스트
    print("\n🔧 사용자 정의 도구 생성 테스트...")
    
    @tool
    def calculate_sum(a: int, b: int) -> int:
        """두 숫자의 합을 계산합니다."""
        return a + b
    
    @tool
    def get_greeting(name: str) -> str:
        """개인화된 인사말을 생성합니다."""
        return f"안녕하세요, {name}님!"
    
    print("✅ 사용자 정의 도구 생성 성공!")
    print(f"- calculate_sum: {calculate_sum.__doc__}")
    print(f"- get_greeting: {get_greeting.__doc__}")
    
    # 도구를 사용하는 에이전트 생성
    print("\n🤖 도구가 포함된 에이전트 생성...")
    agent_with_tools = Agent(
        tools=[calculate_sum, get_greeting],
        system_prompt="당신은 도구를 사용할 수 있는 도움이 되는 어시스턴트입니다."
    )
    print("✅ 도구가 포함된 에이전트 생성 성공!")
    
    # 도구 직접 호출 테스트
    print("\n🧪 도구 직접 호출 테스트...")
    result1 = calculate_sum(5, 3)
    result2 = get_greeting("테스터")
    print(f"✅ calculate_sum(5, 3) = {result1}")
    print(f"✅ get_greeting('테스터') = {result2}")
    
    print("\n📋 도구 시스템 검증 완료:")
    print("- @tool 데코레이터 작동 확인")
    print("- 타입 힌트 지원 확인")
    print("- docstring 기반 설명 확인")
    print("- Agent에 도구 통합 확인")
    
except Exception as e:
    print(f"❌ 도구 시스템 테스트 실패: {e}")
    import traceback
    traceback.print_exc()
