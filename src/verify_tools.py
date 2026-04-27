from tools import get_resource_inventory, search_aws_practices

def verify():
    print("--- 🛠️ Tool Connectivity Test ---")
    
    # Test 1: DynamoDB Tool
    print("Testing DynamoDB Tool...")
    inventory = get_resource_inventory()
    if isinstance(inventory, list):
        print(f"✅ Success: Found {len(inventory)} items in agentic-ai-data-prod.")
    else:
        print(f"❌ DynamoDB Tool Error: {inventory}")

    # Test 2: Search Tool
    print("\nTesting Search Tool...")
    search_result = search_aws_practices("AWS EC2 pricing 2026")
    if search_result:
        print("✅ Success: Search tool returned results.")
    else:
        print("❌ Search Tool Error: No results returned.")

if __name__ == "__main__":
    verify()