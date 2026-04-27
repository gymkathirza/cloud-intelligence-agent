import os
from crewai import Agent, Task, Crew, Process, LLM
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import CloudInventoryTools #fetch_resource_inventory, aws_best_practices_search

# 1. Initialize the LLM (The Brain) [Source 8, 40]
# We use gemini-1.5-flash-latest for optimal performance in 2026
llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.5,
    api_key=os.getenv("GOOGLE_API_KEY")
)

# 2. Define the Agents [Source 10]
data_researcher = Agent(
    role='Senior Data Researcher',
    goal='Extract and summarize cloud usage data from the DynamoDB inventory.',
    backstory="""You are an expert in cloud resource management. You specialize 
    in scanning infrastructure databases to find inefficiencies, such as 
    unused instances or high-cost resources.""",
    tools=[CloudInventoryTools.tools[0]],
    llm=llm,
    allow_delegation=False,
    verbose=True
)

cloud_strategist = Agent(
    role='Cloud Solutions Architect',
    goal='Compare local inventory against AWS best practices and recommend cost optimizations.',
    backstory="""You are a veteran AWS Architect. You take raw data and turn it 
    into actionable business strategies. You use web search to find the 
    latest pricing and optimization whitepapers.""",
    tools=[CloudInventoryTools.tools[1]],
    llm=llm,
    allow_delegation=True,
    verbose=True
)

# 3. Define the Tasks [Source 10, 15]
# Task 1: Data extraction
research_task = Task(
    description="""Scan the 'agentic-ai-data-prod' table using your tools. 
    Identify all resources, their status, and their monthly costs.""",
    expected_output="A structured list of all resources with their current status and cost.",
    agent=data_researcher
)

# Task 2: Strategic Analysis
analysis_task = Task(
    description="""Take the list from the researcher. Search for current 
    AWS cost-optimization best practices (e.g., stopping idle EC2s). 
    Write a brief executive report on how to save money.""",
    expected_output="A 3-paragraph report recommending specific actions to reduce the cloud bill.",
    agent=cloud_strategist
)

# 4. Assemble the Crew [Source 10, 11]
workshop_crew = Crew(
    agents=[data_researcher, cloud_strategist],
    tasks=[research_task, analysis_task],
    process=Process.sequential, # Researcher must finish before Strategist starts
    verbose=True
)