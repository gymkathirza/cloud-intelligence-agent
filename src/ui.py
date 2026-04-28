import streamlit as st
from crew_logic import workshop_crew

st.set_page_config(page_title="Cloud Intelligence Assistant", layout="wide")

st.title("🤖 Agentic AI: Cloud Intelligence Assistant")
st.markdown("""
This agent analyzes your **agentic-ai-data-prod** DynamoDB table and searches 
the web for AWS cost-optimization best practices.
""")

if st.button("🚀 Run Cloud Audit"):
    with st.spinner("The Crew is thinking... (Analyzing DynamoDB and Searching AWS Docs)"):
        try:
            # Kickoff the agent reasoning loop [3]
            result = workshop_crew.kickoff()
            
            st.success("Audit Complete!")
            st.subheader("Executive Summary & Recommendations")
            st.markdown(result)
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.sidebar.info("Built with CrewAI, Gemini 2.5 Flash, Streamlit and Terraform.")