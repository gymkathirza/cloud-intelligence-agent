from crew_logic import workshop_crew

def main():
    print("--- 🚀 Starting the Agentic AI Workshop Crew ---")
    result = workshop_crew.kickoff()
    print("\n\n########################")
    print("## FINAL RECOMMENDATION ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    main()