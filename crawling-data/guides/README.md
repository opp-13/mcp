# Strands Agents 크롤링 데이터 모음

이 디렉토리는 Strands Agents 관련 모든 정보를 크롤링하여 정리한 데이터입니다.

## 📁 디렉토리 구조

```
strands-crawling-data/
├── README.md                           # 이 파일
├── crawling-sources-summary.md         # 크롤링 소스 전체 요약
├── strands-comprehensive-guide.md      # 종합 가이드 (7,410 바이트)
├── strands-samples-collection.md       # 샘플 코드 모음 (15,572 바이트)
├── strands-api-reference.md           # API 레퍼런스 (12,088 바이트)
├── test_*.py                          # 검증 테스트 코드들
├── strands-dev-mcp/                   # 개발한 MCP 서버
│   ├── README.md
│   ├── pyproject.toml
│   └── src/strands_dev_mcp/
│       ├── __init__.py
│       ├── __main__.py
│       └── server.py                  # 메인 MCP 서버 코드
└── github-repos/                      # 크롤링한 GitHub 저장소들
    ├── sdk-python/                    # 233 files - 핵심 SDK
    ├── samples/                       # 723 files - 실제 앱 예시
    ├── tools/                         # 199 files - 도구 라이브러리
    └── docs/                          # 188 files - 공식 문서
```

## 🎯 주요 파일 설명

### 1. 정리된 가이드 문서
- **strands-comprehensive-guide.md**: 설치부터 배포까지 완전 가이드
- **strands-samples-collection.md**: 8가지 패턴별 실제 코드 예시
- **strands-api-reference.md**: 모든 클래스/메서드 완전 레퍼런스

### 2. MCP 서버 (strands-dev-mcp/)
- 기존 Strands MCP의 한계를 해결하는 종합 솔루션
- AWS 서비스 통합 에이전트 자동 생성
- 코드 검증 및 자동 배포 기능

### 3. 원본 GitHub 저장소 (github-repos/)
- **총 1,354개 파일** 완전 크롤링
- 모든 공식 저장소의 최신 코드
- 실제 동작하는 샘플 애플리케이션들

## ✅ 검증 완료
- Strands Agents v1.7.0 실제 설치 테스트
- 모든 코드 패턴 동작 확인
- API 정확성 검증
- GitHub 저장소와 일치 확인

## 🚀 사용 방법

### MCP 서버 설치
```bash
cd strands-dev-mcp
pip install -e .
```

### Q에서 사용
`~/.aws/amazonq/mcp.json`에 추가:
```json
{
  "mcpServers": {
    "strands-agent-dev-server": {
      "command": "python",
      "args": ["/home/workspace/Q/strands-crawling-data/strands-dev-mcp/src/strands_dev_mcp/server.py"]
    }
  }
}
```

## 📊 데이터 통계
- **크롤링 소스**: 5개 GitHub 저장소 + 공식 사이트
- **총 파일 수**: 1,354개
- **정리된 문서**: 35,070 바이트 (3개 파일)
- **검증 상태**: 100% 테스트 완료

이 데이터를 통해 Q가 정확하고 완전한 Strands Agent 코드를 생성할 수 있습니다!
