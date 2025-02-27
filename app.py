import os
import streamlit as st
from dotenv import load_dotenv
from crewai import LLM
from agents import generate_content

# Load env variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title = "AI Blog Writer", page_icon = ":newspaper:", layout = "wide")

# Title and description
st.title("🤖 AI Blog Article Generator, powered by CrewAI")
st.markdown("Generate comprehensive blog posts about any topic using AI agents.")

# Sidebar
with st.sidebar:
    st.header("Content Settings")
    
    # Make the text input take up more space
    topic = st.text_area(
        "Enter your topic",
        height = 100,
        placeholder = "Enter the topic you want to generate content about..."
    )
    
    # Add more sidebar controls if needed
    st.markdown("### Advanced Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    # Add some spacing
    st.markdown("---")
    
    # Make the generate button more prominent in the sidebar
    generate_button = st.button("Generate Article", type="primary", use_container_width=True)
    

if generate_button:
    with st.spinner("Generating content... This may take a moment."):
        try:
            llm = LLM(model = "openai/gpt-4o-mini")
            result = generate_content(llm, topic)
            st.markdown("### Generated Article")
            st.markdown(result)
            
            # Add download button
            st.download_button(
                label = "Download Article",
                data = result.raw,
                file_name = f"{topic.lower().replace(' ', '_')}_article.md",
                mime = "text/markdown"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            
# Footer
st.markdown("---")
st.markdown("Built with CrewAI, Streamlit and powered by OpenAI's GPT4o")