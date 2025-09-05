# Strands Agent 개발 지원 MCP 서버

AWS 서비스를 활용한 Strands Agents 개발을 위한 종합 지원 MCP 서버입니다.

## 🎯 목표

기존 Strands MCP 서버의 한계를 보완하여:

1. **풍부한 정보 제공**: Q가 정확한 Strands 코드를 생성할 수 있도록 상세한 정보 제공
2. **코드 검증**: 생성된 코드의 품질 검증 및 개선 제안
3. **자동 배포**: AWS Lambda/ECS 등으로 완전 자동 배포 (IaC)

## 🚀 주요 기능

### 1. 종합 정보 제공
- **크롤링 기반 최신 정보**: GitHub 저장소, 공식 문서에서 수집한 검증된 정보
- **실제 동작하는 샘플**: 8가지 패턴별 테스트된 코드 예시
- **완전한 API 레퍼런스**: 모든 클래스, 메서드의 상세 정보

### 2. 스마트 코드 생성
- **요구사항 기반 생성**: 자연어 요구사항을 실제 동작하는 코드로 변환
- **AWS 서비스 통합**: S3, DynamoDB, Bedrock 등 자동 통합
- **멀티 에이전트 시스템**: 복잡한 비즈니스 로직을 여러 에이전트로 분할

### 3. 코드 품질 보장
- **문법 검증**: Python 문법 및 Strands 규칙 준수 검사
- **보안 검사**: AWS 보안 베스트 프랙티스 적용
- **성능 최적화**: 비용 효율적인 구현 제안

### 4. 원클릭 배포
- **Lambda 배포**: 서버리스 환경 자동 설정
- **ECS 배포**: 컨테이너 기반 확장 가능한 배포
- **IaC 생성**: CloudFormation/CDK 코드 자동 생성

## 🛠️ 설치 및 사용

### Q Developer CLI에서 사용

`~/.aws/amazonq/mcp.json`에 추가:

```json
{
  "mcpServers": {
    "strands-agent-dev-server": {
      "command": "uvx",
      "args": ["strands-agent-dev-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    }
  }
}
```

### 사용 예시

```
Q: "고객 주문을 처리하고 재고를 확인한 후 결제를 처리하는 멀티 에이전트 시스템을 만들어줘. S3와 DynamoDB를 사용하고 Lambda에 배포하고 싶어."

MCP 서버가 제공하는 것:
1. 상세한 Strands 가이드 및 샘플
2. 요구사항에 맞는 멀티 에이전트 코드 생성
3. AWS 서비스 통합 코드
4. Lambda 배포용 IaC 코드
5. 테스트 코드 및 문서
```

## 🔧 제공 도구

### 정보 제공 도구
- `get_comprehensive_strands_guide()`: 종합 가이드
- `get_strands_samples_collection()`: 샘플 코드 모음
- `get_strands_api_reference()`: API 레퍼런스

### 개발 지원 도구
- `generate_aws_strands_agent()`: AWS 통합 에이전트 생성
- `validate_strands_agent_code()`: 코드 검증 및 리뷰
- `create_multi_agent_system()`: 멀티 에이전트 시스템 설계

### 배포 지원 도구
- `deploy_to_aws()`: AWS 자동 배포

## 📊 기존 Strands MCP vs 개발 지원 MCP

| 기능 | 기존 Strands MCP | 개발 지원 MCP |
|------|------------------|---------------|
| 정보 제공 | 제한적 | 크롤링 기반 풍부한 정보 |
| 코드 생성 | 불가능 | 요구사항 기반 자동 생성 |
| 코드 검증 | 불가능 | 품질/보안/성능 검증 |
| AWS 통합 | 기본 정보만 | 실제 동작하는 통합 코드 |
| 배포 지원 | 없음 | 완전 자동 배포 (IaC) |
| 멀티 에이전트 | 기본 정보만 | 완전한 시스템 설계 |

## 🎯 대상 사용자

- **AWS 서비스를 사용하는 에이전트를 쉽게 구축하고 싶은 개발자**
- **Bedrock Agent의 복잡성을 피하고 싶은 팀**
- **멀티 에이전트 시스템을 빠르게 프로토타이핑하고 싶은 조직**

## 📈 예상 효과

1. **개발 시간 단축**: 수일 → 수시간
2. **코드 품질 향상**: 자동 검증 및 베스트 프랙티스 적용
3. **배포 복잡성 제거**: 원클릭 AWS 배포
4. **학습 곡선 완화**: 풍부한 예시와 가이드

## 🔍 검증된 기반

모든 기능은 다음을 기반으로 검증되었습니다:

- ✅ Strands Agents v1.7.0 실제 테스트
- ✅ GitHub 공식 저장소 크롤링 데이터
- ✅ 실제 동작하는 샘플 코드
- ✅ AWS 서비스 통합 테스트

## 🚀 시작하기

1. MCP 서버 설치 및 설정
2. Q에서 "Strands Agent 가이드를 보여줘" 요청
3. 요구사항에 맞는 에이전트 생성 요청
4. 생성된 코드 검증 및 배포

**기존 Strands MCP의 한계를 완전히 해결하는 종합 솔루션입니다!**
