"""
Example: Using CloudInventoryTools with CrewAI Agents

This shows how to properly integrate the @tool decorated functions with CrewAI.
"""
from crewai import Agent, Task, Crew
from tools import fetch_resource_inventory, aws_best_practices_search

# Create an agent that has access to the tools
inventory_agent = Agent(
    role="Cloud Inventory Specialist",
    goal="Analyze cloud resources and provide optimization recommendations",
    backstory="Expert in AWS resource management and cost optimization",
    tools=[fetch_resource_inventory, aws_best_practices_search],
    verbose=True
)

# Create tasks that use the agent and tools
task_1 = Task(
    description="Fetch all cloud resources from the inventory and provide a summary",
    agent=inventory_agent,
    expected_output="A comprehensive list of all cloud resources with their costs"
)

task_2 = Task(
    description="Search for AWS best practices for cost optimization and provide recommendations",
    agent=inventory_agent,
    expected_output="Top recommendations for cost optimization based on current AWS best practices"
)

# Create a crew and execute tasks
crew = Crew(
    agents=[inventory_agent],
    tasks=[task_1, task_2],
    verbose=True
)

if __name__ == "__main__":
    # Run the crew
    result = crew.kickoff()
    print("\n=== Final Report ===")
    print(result)
