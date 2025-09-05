# Q Rule - Strands Agent MCP 서버 개발 지침

당신은 AWS 서비스 기반 Strands Agent 개발을 위한 MCP 서버를 구축하는 전문 개발자입니다.

## 🎯 프로젝트 목표
기존 Strands MCP 서버의 한계(제한적 정보 제공)를 해결하여, Q가 정확하고 완전한 Strands Agent 코드를 생성할 수 있도록 지원하는 종합 MCP 서버를 개발합니다.

## 📋 핵심 개발 원칙

### 1. PEP 8 코드 컨벤션 (필수 준수)

#### 1.1 네이밍 컨벤션
```python
# 변수, 함수: snake_case
user_name = "john"
def generate_agent_code():
    pass

# 클래스: PascalCase  
class CodeGenerator:
    pass

# 상수: UPPER_SNAKE_CASE
MAX_RETRY_COUNT = 3
AWS_DEFAULT_REGION = "us-west-2"

# 비공개 변수/함수: 앞에 언더스코어
def _internal_helper():
    pass
_private_var = "secret"
```

#### 1.2 라인 길이 및 들여쓰기
```python
# 라인 길이: 최대 88자 (Black 기준)
# 들여쓰기: 4칸 스페이스 (탭 금지)

def long_function_name(
    parameter_one: str,
    parameter_two: int,
    parameter_three: Optional[List[str]] = None
) -> Dict[str, Any]:
    """긴 함수 시그니처는 이렇게 분할"""
    if parameter_three is None:
        parameter_three = []
    
    return {
        "result": "success",
        "data": parameter_one,
        "count": parameter_two
    }
```

#### 1.3 Import 순서 (PEP 8 + isort)
```python
# 1. 표준 라이브러리
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# 2. 서드파티 라이브러리  
import boto3
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

# 3. 로컬 모듈
from .core.code_generator import CodeGenerator
from .utils.aws_helper import create_s3_client
```

#### 1.4 공백 및 연산자
```python
# 연산자 주변 공백
x = 1
y = 2
result = x + y

# 함수 호출 시 공백 없음
function_call(arg1, arg2)

# 리스트, 딕셔너리
my_list = [1, 2, 3, 4]
my_dict = {"key": "value", "number": 42}

# 슬라이싱 시 공백 없음
text[1:4]
items[start:end:step]
```

#### 1.5 문자열 처리
```python
# f-string 우선 사용
name = "World"
message = f"Hello, {name}!"

# 긴 문자열은 괄호로 묶어서 분할
long_message = (
    "이것은 매우 긴 메시지입니다. "
    "여러 줄에 걸쳐 작성할 때는 "
    "이렇게 괄호를 사용합니다."
)

# 멀티라인 문자열
sql_query = """
SELECT *
FROM users
WHERE active = true
  AND created_at > %s
"""
```

### 2. 코드 품질 원칙

#### 2.1 타입 힌트 (PEP 484, 526)
```python
from typing import Dict, List, Any, Optional, Union

def process_data(
    input_data: List[Dict[str, Any]],
    config: Optional[Dict[str, str]] = None
) -> Dict[str, Union[str, int]]:
    """모든 함수에 타입 힌트 필수"""
    if config is None:
        config = {}
    
    result: Dict[str, Union[str, int]] = {
        "status": "success",
        "count": len(input_data)
    }
    return result
```

#### 2.2 Docstring (PEP 257 + Google Style)
```python
def generate_strands_agent(
    requirements: str,
    aws_services: List[str],
    agent_type: str = "basic"
) -> Dict[str, Any]:
    """
    요구사항을 바탕으로 Strands Agent 코드를 생성합니다.
    
    Args:
        requirements: 에이전트 요구사항 (자연어로 상세히 기술)
        aws_services: 사용할 AWS 서비스 목록 (예: ["s3", "dynamodb"])
        agent_type: 에이전트 타입 ("basic", "multi_agent", "conversational")
        
    Returns:
        생성된 코드와 메타데이터를 포함한 딕셔너리:
        {
            "success": bool,
            "data": {
                "code": str,
                "requirements_txt": str,
                "readme": str
            },
            "metadata": dict
        }
        
    Raises:
        ValueError: 잘못된 요구사항이 입력된 경우
        AWSError: AWS 서비스 연결 실패 시
        
    Example:
        >>> result = generate_strands_agent(
        ...     requirements="간단한 챗봇을 만들어주세요",
        ...     aws_services=["bedrock"],
        ...     agent_type="basic"
        ... )
        >>> print(result["success"])
        True
    """
    pass
```

#### 2.3 에러 처리 및 로깅
```python
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def safe_function(data: str) -> Dict[str, Any]:
    """안전한 함수 구현 패턴"""
    try:
        # 입력 검증
        if not data or not isinstance(data, str):
            raise ValueError("Invalid input data")
        
        # 메인 로직
        result = process_data(data)
        logger.info(f"Successfully processed data: {len(data)} characters")
        
        return {
            "success": True,
            "data": result,
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "input_length": len(data)
            }
        }
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return {
            "success": False,
            "error": str(e),
            "error_type": "ValidationError"
        }
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return {
            "success": False,
            "error": "Internal server error",
            "error_type": type(e).__name__
        }
```

### 3. MCP 서버 구조 원칙

#### 3.1 도구 함수 구조 (PEP 8 준수)
```python
@mcp.tool()
def generate_strands_agent(
    requirements: str,
    aws_services: Optional[List[str]] = None,
    agent_type: str = "basic",
    deployment_target: str = "lambda"
) -> Dict[str, Any]:
    """
    요구사항을 바탕으로 Strands Agent 코드를 생성합니다.
    
    이 도구는 사용자의 자연어 요구사항을 분석하여 즉시 실행 가능한
    완전한 Strands Agent 프로젝트를 생성합니다.
    """
    # 입력 검증 (PEP 8 스타일)
    if not requirements or not requirements.strip():
        return {
            "success": False,
            "error": "요구사항이 비어있습니다.",
            "suggestions": [
                "구체적인 에이전트 기능을 설명해주세요.",
                "예: '고객 문의를 처리하는 챗봇을 만들어주세요'"
            ]
        }
    
    # 기본값 설정
    if aws_services is None:
        aws_services = ["bedrock"]
    
    try:
        # 코드 생성 로직
        generator = CodeGenerator()
        generated_code = generator.create_agent(
            requirements=requirements,
            services=aws_services,
            agent_type=agent_type
        )
        
        # 성공 응답
        return {
            "success": True,
            "data": {
                "main_code": generated_code.main_file,
                "requirements_txt": generated_code.requirements,
                "readme_md": generated_code.readme,
                "deployment_config": generated_code.deployment
            },
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "version": "0.1.0",
                "agent_type": agent_type,
                "aws_services": aws_services,
                "deployment_target": deployment_target
            }
        }
        
    except Exception as e:
        logger.exception(f"Agent generation failed: {e}")
        return {
            "success": False,
            "error": f"코드 생성 중 오류가 발생했습니다: {str(e)}",
            "error_type": type(e).__name__,
            "suggestions": [
                "요구사항을 더 구체적으로 작성해보세요.",
                "지원되는 AWS 서비스인지 확인해보세요."
            ]
        }
```

### 4. 클래스 설계 원칙

#### 4.1 클래스 구조 (PEP 8)
```python
class CodeGenerator:
    """Strands Agent 코드 생성기 클래스"""
    
    # 클래스 상수
    DEFAULT_MODEL = "anthropic.claude-3-5-sonnet-20241022-v2:0"
    DEFAULT_REGION = "us-west-2"
    SUPPORTED_SERVICES = ["bedrock", "s3", "dynamodb", "lambda"]
    
    def __init__(self, templates_path: Optional[str] = None) -> None:
        """
        코드 생성기를 초기화합니다.
        
        Args:
            templates_path: 템플릿 파일 경로 (기본값: None)
        """
        self._templates_path = templates_path or "templates"
        self._template_env = self._setup_template_environment()
        self._logger = logging.getLogger(self.__class__.__name__)
    
    def _setup_template_environment(self) -> Environment:
        """템플릿 환경을 설정합니다 (비공개 메서드)"""
        return Environment(
            loader=FileSystemLoader(self._templates_path),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def generate_basic_agent(
        self,
        requirements: str,
        aws_services: List[str]
    ) -> GeneratedCode:
        """기본 에이전트 코드를 생성합니다 (공개 메서드)"""
        self._logger.info(f"Generating basic agent for: {requirements[:50]}...")
        
        # 구현 로직
        template = self._template_env.get_template("basic_agent.py.j2")
        code = template.render(
            requirements=requirements,
            aws_services=aws_services,
            model_id=self.DEFAULT_MODEL,
            region=self.DEFAULT_REGION
        )
        
        return GeneratedCode(
            main_file=code,
            requirements=self._generate_requirements(aws_services),
            readme=self._generate_readme(requirements)
        )
```

### 5. 코드 검증 도구 설정

#### 5.1 필수 도구 설정
```python
# pyproject.toml에 추가할 설정

[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["strands_agent_mcp"]

[tool.pylint.messages_control]
disable = [
    "C0330",  # Wrong hanging indentation (black이 처리)
    "C0326",  # Bad whitespace (black이 처리)
]

[tool.pylint.format]
max-line-length = "88"

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
```

### 6. 필수 준수사항 체크리스트

#### 코드 작성 시 반드시 확인할 것
- [ ] **PEP 8 네이밍**: snake_case, PascalCase, UPPER_SNAKE_CASE 준수
- [ ] **라인 길이**: 88자 이하 유지
- [ ] **들여쓰기**: 4칸 스페이스 (탭 금지)
- [ ] **Import 순서**: 표준 → 서드파티 → 로컬
- [ ] **타입 힌트**: 모든 함수, 변수에 적용
- [ ] **Docstring**: Google 스타일로 상세 작성
- [ ] **에러 처리**: try-except 블록 적용
- [ ] **로깅**: 적절한 로그 레벨 사용
- [ ] **상수**: 하드코딩 금지, 상수로 정의
- [ ] **함수 길이**: 한 함수당 50줄 이하 권장

#### 금지사항
- ❌ 탭 문자 사용 (스페이스만 사용)
- ❌ 라인 끝 공백
- ❌ 불필요한 공백 라인
- ❌ 매직 넘버 (상수로 정의할 것)
- ❌ 전역 변수 (클래스 상수 또는 설정 파일 사용)
- ❌ 긴 함수 (50줄 초과 시 분할)

## 🔧 코드 품질 검증 명령어

개발 중 다음 명령어로 코드 품질을 검증하세요:

```bash
# 코드 포맷팅
black src/ tests/
isort src/ tests/

# 타입 검사
mypy src/

# 코드 품질 검사
pylint src/

# 테스트 실행
pytest tests/ --cov=src/
```

이 PEP 8 규칙을 엄격히 준수하여 일관되고 읽기 쉬운 고품질 코드를 작성하세요!
