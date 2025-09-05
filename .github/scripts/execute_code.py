import json
import boto3
import os
import subprocess
import re
import requests

agent_arn = os.environ['AGENT_ARN']
slack_webhook = os.environ.get('SLACK_WEBHOOK_URL')

# PR 단위로 변경된 파일 가져오기
try:
    # GitHub Actions에서 PR의 base와 head 비교
    base_sha = os.environ.get('GITHUB_BASE_REF', 'main')
    result = subprocess.run(['git', 'diff', '--name-only', f'origin/{base_sha}...HEAD'], capture_output=True, text=True)
    changed_files = [f for f in result.stdout.strip().split('\n')
                     if f.startswith('dev/') and f.endswith('.py')]
except:
    changed_files = []

if not changed_files:
    print("No changed Python files in /dev folder")
    exit(0)

print(f"📁 Found {len(changed_files)} changed files: {changed_files}")

agent_core_client = boto3.client('bedrock-agentcore')

# 각 파일별로 개별 처리
for file_path in changed_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'boto3' not in content:
            continue

        # 1줄로 변환
        one_line = re.sub(r'\n\s*', '; ', content.strip())
        one_line = re.sub(r';\s*;', ';', one_line)

        print(f"🔄 Processing: {file_path}")

        # Bedrock Agent 호출
        payload = json.dumps({"prompt": one_line}).encode()
        response = agent_core_client.invoke_agent_runtime(
            agentRuntimeArn=agent_arn,
            payload=payload
        )

        content_chunks = []
        for chunk in response.get("response", []):
            content_chunks.append(chunk.decode('utf-8'))

        result = ''.join(content_chunks)

        print(f"✅ {file_path}: {result[:100]}...")

        # 개별 Slack 알림
        if slack_webhook:
            slack_message = {
                "text": f"🤖 *{file_path}*\n📋 Result: {result[:400]}..."
            }
            requests.post(slack_webhook, json=slack_message)

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        if slack_webhook:
            requests.post(slack_webhook, json={
                "text": f"❌ Error processing {file_path}: {str(e)}"
            })

print("🎉 All files processed")