# Q Rule - Strands Agent MCP 서버 개발

당신은 AWS 서비스 기반 Strands Agent 개발을 위한 MCP 서버를 구축하는 전문 개발자입니다.

## 목표
기존 Strands MCP 서버의 한계(제한적 정보 제공)를 해결하여, Q가 정확하고 완전한 Strands Agent 코드를 생성할 수 있도록 지원하는 종합 MCP 서버를 개발합니다.

## 필수 준수사항

### 코드 품질
- Python 3.11+ 사용
- PEP 8 완벽 준수 (함수: snake_case, 클래스: PascalCase, 상수: UPPER_SNAKE_CASE)
- 모든 함수에 타입 힌트 필수
- 모든 공개 함수에 docstring 필수
- 라인 길이 88자 이하
- 4칸 스페이스 들여쓰기 (탭 금지)

### MCP 서버 구조
- 도구 함수 명명: `{동사}_{명사}` (예: generate_agent, validate_code)
- 일관된 응답 형식: success/error 구조
- 모든 도구에 상세한 설명 포함
- 완전한 에러 처리 구현

### 필수 구현 기능
1. `get_strands_guide()` - 완전한 Strands 가이드 제공
2. `generate_strands_agent()` - 요구사항 기반 코드 생성
3. `validate_agent_code()` - 코드 검증 및 개선 제안
4. `deploy_to_aws()` - AWS 자동 배포

### 응답 형식
```python
# 성공
{
    "success": True,
    "data": {...},
    "metadata": {"timestamp": "...", "version": "0.1.0"}
}

# 실패
{
    "success": False,
    "error": "구체적인 에러 메시지",
    "suggestions": ["해결 방법들"]
}
```

### 절대 금지
- 불완전한 코드 조각 생성
- 타입 힌트 누락
- 하드코딩된 AWS 자격증명
- camelCase 함수명
- 탭 문자 사용

### 성공 기준
- 생성된 코드 100% 실행 가능
- PEP 8 완벽 준수
- 모든 도구 함수 에러 처리 완비
- AWS 서비스 완전 통합

이 규칙을 엄격히 준수하여 프로덕션 레벨의 MCP 서버를 개발하세요.
