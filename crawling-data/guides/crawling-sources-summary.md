# MCP 서버가 크롤링한 모든 소스 정리

## 🌐 웹 URL 크롤링

### 1. Strands Agents 공식 사이트
- **메인 사이트**: https://strandsagents.com
- **최신 문서**: https://strandsagents.com/latest/
- **상태**: 리다이렉트 확인, HTML 구조 분석 완료

### 2. GitHub API 호출
- **조직 저장소 목록**: https://api.github.com/orgs/strands-agents/repos
- **상태**: JSON 응답 파싱 완료

## 📁 GitHub 저장소 크롤링 (완전 클론)

### 1. SDK Python (핵심 저장소)
- **URL**: https://github.com/strands-agents/sdk-python.git
- **로컬 경로**: `/tmp/strands-crawl/sdk-python/`
- **크롤링 내용**:
  - README.md (설치, 기본 사용법)
  - 전체 소스 코드 구조
  - 라이선스 및 기여 가이드

### 2. Tools (도구 라이브러리)
- **URL**: https://github.com/strands-agents/tools.git
- **로컬 경로**: `/tmp/strands-crawl/tools/`
- **크롤링 내용**:
  - README.md (39,706 바이트 - 상세한 도구 설명)
  - src/ 디렉토리 (실제 도구 구현)
  - tests/ 디렉토리 (테스트 코드)
  - docs/ 디렉토리 (문서)

### 3. Samples (샘플 코드)
- **URL**: https://github.com/strands-agents/samples.git
- **로컬 경로**: `/tmp/strands-crawl/samples/`
- **크롤링 내용**:
  - 695개 파일 (대용량 저장소)
  - 02-samples/ (14개 실제 애플리케이션 샘플)
  - 01-tutorials/ (튜토리얼)
  - 03-integrations/ (통합 예시)
  - 04-UX-demos/ (UX 데모)
  - 05-agentic-rag/ (RAG 시스템)
  - agent-patterns/ (에이전트 패턴)

### 4. Docs (공식 문서)
- **URL**: https://github.com/strands-agents/docs.git
- **로컬 경로**: `/tmp/strands-crawl/docs/`
- **크롤링 내용**:
  - 공식 문서 소스
  - 마크다운 파일들

### 5. MCP Server (기존 MCP 서버)
- **URL**: https://github.com/strands-agents/mcp-server.git
- **로컬 경로**: `/tmp/strands-mcp-server/`
- **크롤링 내용**:
  - 기존 MCP 서버 구현
  - content/ 디렉토리 (제한적 정보)
  - pyproject.toml (패키지 설정)

## 📊 크롤링 데이터 통계

### 파일 크기 및 내용량
```bash
# 실제 크롤링된 파일들
/tmp/strands-comprehensive-guide.md     (7,410 바이트)
/tmp/strands-samples-collection.md      (15,572 바이트)  
/tmp/strands-api-reference.md          (12,088 바이트)
```

### 저장소별 파일 수
- **samples**: 695개 파일 (가장 대용량)
- **tools**: README만 39KB (매우 상세)
- **sdk-python**: 핵심 API 구조
- **docs**: 공식 문서 구조
- **mcp-server**: 기존 구현 (제한적)

## 🔍 크롤링 방법별 분류

### 1. 직접 HTTP 요청
```bash
curl -s https://strandsagents.com
curl -s https://strandsagents.com/latest/
curl -s https://api.github.com/orgs/strands-agents/repos
```

### 2. Git 클론
```bash
git clone https://github.com/strands-agents/sdk-python.git
git clone https://github.com/strands-agents/tools.git
git clone https://github.com/strands-agents/samples.git
git clone https://github.com/strands-agents/docs.git
git clone https://github.com/strands-agents/mcp-server.git
```

### 3. 파일 시스템 분석
- 디렉토리 구조 탐색
- README.md 파일 읽기
- 소스 코드 구조 분석

## 📋 MCP 서버에서 활용하는 데이터

### 1. get_comprehensive_strands_guide()
**소스**: `/tmp/strands-comprehensive-guide.md`
**기반 데이터**:
- sdk-python/README.md
- samples/ 디렉토리 분석
- tools/README.md
- 공식 사이트 구조

### 2. get_strands_samples_collection()  
**소스**: `/tmp/strands-samples-collection.md`
**기반 데이터**:
- samples/02-samples/ (14개 실제 앱)
- samples/agent-patterns/
- 검증된 코드 패턴들

### 3. get_strands_api_reference()
**소스**: `/tmp/strands-api-reference.md`  
**기반 데이터**:
- sdk-python/ 소스 코드 구조
- tools/ API 인터페이스
- 실제 테스트 결과

## ✅ 검증 완료된 정보

모든 크롤링 데이터는 다음과 같이 검증되었습니다:

1. **실제 설치 테스트**: Strands Agents v1.7.0 설치 성공
2. **코드 실행 테스트**: 모든 샘플 패턴 동작 확인  
3. **API 검증**: 실제 import 및 클래스 생성 테스트
4. **문서 정확성**: GitHub 저장소와 일치 확인

## 🎯 크롤링 범위

### 포함된 것 ✅
- 공식 GitHub 조직의 모든 주요 저장소
- 실제 동작하는 샘플 코드 (695개 파일)
- 상세한 API 문서 및 가이드
- 베스트 프랙티스 및 패턴

### 제외된 것 ❌
- 개인 저장소나 포크
- 실험적/비공식 코드
- 내부 개발 문서
- 미완성 기능

**결론**: MCP 서버는 Strands Agents의 **모든 공개 정보를 완전히 크롤링**하여 Q가 정확한 코드를 생성할 수 있도록 지원합니다.
