import boto3
import uuid
from datetime import datetime

def create_dev_bucket():
    """개발용 S3 버킷 생성"""
    s3_client = boto3.client('s3')
    bucket_name = f"dev-bucket-{str(uuid.uuid4())[:8]}"

    s3_client.create_bucket(Bucket=bucket_name)
    print(f"개발용 버킷 생성됨: {bucket_name}")

    # 개발용 태그 추가
    s3_client.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            'TagSet': [
                {'Key': 'Environment', 'Value': 'Development'}, 
                {'Key': 'CreatedBy', 'Value': 'GitHubActions'},
                {'Key': 'CreatedDate', 'Value': datetime.now().strftime('%Y-%m-%d')}
            ]
        }
    )

    return bucket_name

if __name__ == "__main__":
    bucket = create_dev_bucket()
    print(f"✅ Dev bucket ready: {bucket}")