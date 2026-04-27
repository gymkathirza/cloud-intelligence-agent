import os
import boto3
from langchain_google_genai import ChatGoogleGenerativeAI

def test_connections():
    print("--- Testing Connections ---")
    
    # 1. Test Gemini
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
        response = llm.invoke("Say 'Gemini is connected!'")
        print(f"✅ Brain: {response.content}")
    except Exception as e:
        print(f"❌ Brain Error: {e}")

    # 2. Test AWS
    try:
        # This checks if boto3 can see your secrets
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print(f"✅ AWS: Connected as {identity['Arn']}")
    except Exception as e:
        print(f"❌ AWS Error: {e}")

if __name__ == "__main__":
    test_connections()