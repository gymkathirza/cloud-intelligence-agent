import os
import boto3
from typing import TYPE_CHECKING
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

if TYPE_CHECKING:
    from boto3.resources.base import ServiceResource

# Initialize the Search Tool
search_tool = DuckDuckGoSearchRun()

# ============================================================================
# Core Implementation Functions (without decorators - used directly and by agents)
# ============================================================================

def _fetch_resource_inventory_impl():
    """
    Core implementation: Fetches all cloud resources from the DynamoDB inventory table.
    Returns ResourceId, ResourceType, Status, and MonthlyCost.
    """
    table_name = "agentic-ai-data-prod"
    region = os.getenv("AWS_REGION", "us-east-1")
    
    dynamodb: 'ServiceResource' = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(table_name)  # type: ignore
    
    try:
        response = table.scan()
        items = response.get('Items', [])
        return items if items else "The inventory is currently empty."
    except Exception as e:
        return f"Error accessing DynamoDB: {str(e)}"

def _aws_best_practices_search_impl(query: str):
    """
    Core implementation: Searches the web for AWS best practices and pricing updates.
    """
    return search_tool.run(query)

# ============================================================================
# CrewAI Tool Definitions (with @tool decorator for agent usage)
# ============================================================================

@tool
def fetch_resource_inventory():
    """
    Fetches all cloud resources from the DynamoDB inventory table.
    Returns ResourceId, ResourceType, Status, and MonthlyCost.
    Use this tool to analyze current resource allocation and costs.
    """
    return _fetch_resource_inventory_impl()

@tool
def aws_best_practices_search(query: str):
    """
    Searches the web for the latest AWS documentation, best practices, 
    and pricing updates related to specific cloud resources.
    Use this tool to find optimization recommendations.
    """
    return _aws_best_practices_search_impl(query)

# ============================================================================
# Helper Functions (for direct testing without CrewAI)
# ============================================================================

def get_resource_inventory():
    """Direct call version for testing without CrewAI."""
    return _fetch_resource_inventory_impl()

def search_aws_practices(query: str):
    """Direct call version for testing without CrewAI."""
    return _aws_best_practices_search_impl(query)

# ============================================================================
# CrewAI Toolset Collection
# ============================================================================

class CloudInventoryTools:
    """Collection of CrewAI tools for cloud operations."""
    tools = [fetch_resource_inventory, aws_best_practices_search]