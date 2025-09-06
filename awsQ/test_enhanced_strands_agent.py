from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import use_aws, calculator, python_repl
import json
import logging

# Fast-LLM-Agent-MCP 패턴을 참고한 향상된 모델 설정
MODEL = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"

bedrock_model = BedrockModel(
    model_id=MODEL,
    temperature=0.3,
    top_p=0.8,
)

# 로깅 설정 (Strands 문서 권장)
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

@tool
def enhanced_aws_analyzer(resource_type: str) -> str:
    """
    향상된 AWS 리소스 분석기
    
    Args:
        resource_type (str): 분석할 AWS 리소스 타입 (ec2, s3, rds 등)
    
    Returns:
        str: 분석 결과 및 권장사항
    """
    try:
        if not isinstance(resource_type, str):
            return "Error: resource_type must be a string"
        
        resource_type = resource_type.lower().strip()
        
        analysis_templates = {
            "s3": "S3 버킷 분석: 스토리지 클래스, 암호화, 퍼블릭 액세스 설정 검토",
            "ec2": "EC2 인스턴스 분석: 인스턴스 타입, 보안 그룹, 비용 최적화 검토",
            "rds": "RDS 분석: 데이터베이스 성능, 백업 설정, 보안 구성 검토"
        }
        
        if resource_type in analysis_templates:
            return f"✅ {analysis_templates[resource_type]}"
        else:
            return f"⚠️ 지원되지 않는 리소스 타입: {resource_type}. 지원 타입: {', '.join(analysis_templates.keys())}"
            
    except Exception as e:
        return f"❌ 분석 중 오류 발생: {str(e)}"

# AWS Strands Demo + Fast-LLM-Agent 패턴을 결합한 향상된 Agent
agent = Agent(
    model=bedrock_model,  # 향상된 모델 설정 사용
    tools=[
        use_aws,
        calculator, 
        python_repl,
        enhanced_aws_analyzer
    ],
    system_prompt="""
    당신은 AWS 전문가 어시스턴트입니다. 다음 원칙을 따르세요:
    
    1. 🔍 체계적 분석: 단계별로 AWS 리소스를 분석합니다
    2. 💰 비용 최적화: 항상 비용 효율성을 고려합니다  
    3. 🔒 보안 우선: 보안 설정을 우선적으로 검토합니다
    4. 📊 데이터 기반: 실제 데이터를 바탕으로 권장사항을 제시합니다
    5. ⚡ 성능 최적화: 성능 개선 방안을 제안합니다
    
    오류 발생 시 명확한 해결책을 제시하고, 모든 작업을 로그로 기록합니다.
    """
)

if __name__ == "__main__":
    try:
        print("=== 2단계: 향상된 MCP 패턴 + 추가 도구 조합 ===")
        
        query = """
        다음 작업을 체계적으로 수행해주세요:
        
        1. 🔍 AWS S3 버킷 전체 조회
        2. 💰 각 버킷의 예상 비용 계산
        3. 🔒 보안 설정 상세 분석
        4. 📊 종합 리포트 생성
        5. ⚡ 최적화 권장사항 제시
        """
        
        result = agent(query)
        print(result.message)
        
    except Exception as e:
        print(f"❌ Agent 실행 중 오류 발생: {e}")
        print("🔧 문제 해결 방법:")
        print("1. AWS 자격 증명 확인")
        print("2. Bedrock 모델 액세스 권한 확인")
        print("3. 네트워크 연결 상태 확인")
