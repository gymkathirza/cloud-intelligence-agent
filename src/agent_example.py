"""
Example: Using CloudInventoryTools with CrewAI Agents and Google Gemini.

This script explicitly passes a ChatGoogleGenerativeAI LLM so CrewAI does not
fall back to the OpenAI provider and require OPENAI_API_KEY.
"""
import os
from crewai import Agent, Task, Crew
from crewai.llms.providers.gemini.completion import GeminiCompletion
from tools import fetch_resource_inventory, aws_best_practices_search

# 1. Initialize the LLM using CrewAI's native Gemini provider
llm = GeminiCompletion(
    model="gemini-2.5-flash",
    temperature=0.5,
    api_key=os.getenv("GOOGLE_API_KEY"),
    provider="google"
)

# 2. Define agents with explicit Google Gemini LLM and CrewAI tools
inventory_agent = Agent(
    role="Cloud Inventory Specialist",
    goal="Analyze cloud resources and provide optimization recommendations",
    backstory="Expert in AWS resource management and cost optimization.",
    tools=[fetch_resource_inventory],
    llm=llm,
    allow_delegation=False,
    verbose=True
)

search_agent = Agent(
    role="Cloud Strategy Researcher",
    goal="Compare inventory data against AWS best practices and recommend optimizations.",
    backstory="You are a cloud strategy expert who uses the latest best practices to reduce costs and improve architecture.",
    tools=[aws_best_practices_search],
    llm=llm,
    allow_delegation=True,
    verbose=True
)

# 3. Create tasks that use these agents
task_1 = Task(
    description="Fetch all cloud resources from the inventory and provide a summary",
    agent=inventory_agent,
    expected_output="A comprehensive list of all cloud resources with their costs"
)

task_2 = Task(
    description="Search for AWS best practices for cost optimization and provide recommendations",
    agent=search_agent,
    expected_output="Top recommendations for cost optimization based on current AWS best practices"
)

# 4. Execute the crew
crew = Crew(
    agents=[inventory_agent, search_agent],
    tasks=[task_1, task_2],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== Final Report ===")
    print(result)
