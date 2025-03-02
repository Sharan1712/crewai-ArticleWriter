import os
import streamlit as st
# from dotenv import load_dotenv
from crewai import LLM
from agents import generate_content

# Load env variables
# load_dotenv()

# Streamlit Page Config
st.set_page_config(
    page_title = "AI Blog Writer", 
    page_icon = ":newspaper:", 
    layout = "wide",
    initial_sidebar_state="expanded")

# Logo
st.logo(
    "https://cdn.prod.website-files.com/66cf2bfc3ed15b02da0ca770/66d07240057721394308addd_Logo%20(1).svg",
    link = "https://www.crewai.com/",
    size = "large"
)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    # Title and description
    st.title("✍️AI Blog Article Generator, powered by :red[CrewAI]")
    st.markdown("Generate comprehensive blog posts about any topic using AI agents.")

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Model API Configuration")
    st.write("")
    
    model_options = [
        "gpt-4o-mini",
        "gpt-4o",
        "o1",
        "o1-mini", 
        "o1-preview"
        "o3-mini"
    ]
    
    selected_model = st.selectbox("🤖 Select which LLM to use", model_options, key = "selected_model")
    
    with st.expander("🔑 API Keys", expanded = True):
        
        st.info("API keys are stored temporarily in memory and cleared when you close the browser.")
        
        openai_api_key = st.text_input(
            "OpenAI API Key",
            type = "password",
            placeholder = "Enter your OpenAI API key",
            help = "Enter your OpenAI API key"
        )
        
        if openai_api_key:
            os.environ["OPENAI_API_KEY"] = openai_api_key
            
        serper_api_key = st.text_input(
            "Serper API Key",
            type = "password",
            placeholder = "Enter your Serper API key",
            help = "Enter your Serper API key for web search capabilities"
            )
        if serper_api_key:
            os.environ["SERPER_API_KEY"] = serper_api_key
    
    st.write("")
    with st.expander("ℹ️ About", expanded=False):
        st.markdown(
            """This Blog Article Writing assistant uses advanced AI models to help you:
                - Research any topic in depth
                - Analyze and summarize information
                - Provide structured article
                
                Choose your preferred model and enter the required API keys to get started.""")

if not os.environ.get("OPENAI_API_KEY"):
    st.warning("⚠️ Please enter your OpenAI API key in the sidebar to get started")
    st.stop()

if not os.environ.get("SERPER_API_KEY"):
    st.warning("⚠️ Please enter your Serper API key in the sidebar to get started")
    st.stop()

# Create two columns for the input section
input_col1, input_col2, input_col3 = st.columns([1, 6, 1])

with input_col2:
    # st.header("Content Settings")
    
    # Make the text input take up more space
    topic = st.text_area(
        "Enter your topic",
        height = 68,
        placeholder = "Enter the topic you want to generate content about..."                
    )

col1, col2, col3 = st.columns([1, 0.5, 1])
with col2:
    generate_button = st.button("🚀 Generate Article", use_container_width = False, type = "primary")    

    # # Add more sidebar controls if needed
    # st.markdown("### Advanced Settings")
    # temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    # # Add some spacing
    # st.markdown("---")
    
    # # Make the generate button more prominent in the sidebar
    # generate_button = st.button("Generate Article", type="primary", use_container_width=True)
    

if generate_button:
    with st.spinner("Generating content... This may take a moment."):
        try:
            llm = LLM(model = f"openai/{selected_model}")
            result = generate_content(llm, topic)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            
    st.markdown("### Generated Article")
    st.markdown(str(result))
            
    # Add download button
    st.download_button(
        label = "Download Article",
        data = result.raw,
        file_name = f"{topic.lower().replace(' ', '_')}_article.md",
        mime = "text/markdown"
        )
    
# Add footer
st.divider()
footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])
with footer_col2:
    st.caption("Made with ❤️ using [CrewAI](https://crewai.com), [Serper](https://serper.dev/) and [Streamlit](https://streamlit.io)")
    st.caption("By Sharan Shyamsundar")
            
# Footer
# footer_html = """<div style='text-align: center;'>
#   <p>Developed with CrewAI, Streamlit and OpenAI by Sharan</p>
# </div>"""
# st.markdown(footer_html, unsafe_allow_html=True)

# st.markdown("Built with CrewAI, Streamlit and powered by OpenAI's GPT4o")