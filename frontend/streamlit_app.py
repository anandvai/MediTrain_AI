import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Menu configuration (1=sidebar menu, 2=horizontal menu)
MENU_TYPE = 1

# Function to set up the menu
def streamlit_menu(menu_type=1):
    if menu_type == 1:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home","Description", "Meditrain AI Bot"],
                icons=["house", "robot", "book"],
                menu_icon="cast",
                default_index=0,
                key="sidebar_menu",
            )
        return selected

# Initialize the menu
selected = streamlit_menu(menu_type=MENU_TYPE)

# Pages
if selected == "Home":
    st.title(" Welcome to MediTrain AI Empowering the Doctor Today And Tommorow!")
    st.subheader("Empowering Healthcare Education Through AI")
    st.markdown("""
        **MediTrain AI** is your AI-powered healthcare assistant designed to enhance medical education and patient communication. 
        Use the navigation menu to explore features like:
        - **Interactive Chatbot**: Simulate real-time patient conversations.
        - **Health Resources**: Access valuable information on health checkups and tips.
        - **Learn and Explore**: Discover insights on healthcare technologies.
    """)

elif selected == "Meditrain AI Bot":
    
   
    try:
        bot = importlib.import_module("bot")
        if hasattr(bot, "chatbot_interface"):
            bot.chatbot_interface()
        else:
            st.error("The bot module does not have a 'chatbot_interface' function.")
    except Exception as e:
        st.error(f"Error loading the chatbot interface: {e}")

elif selected == "Description":
    st.title("Description")
    st.markdown("""
        ### About MediTrain AI
        MediTrain AI is designed to empower users with the ability to simulate medical interactions and access health-related information efficiently.

        ### How It Works
        - **Chatbot Feature**: Built using AI models trained on medical datasets, the bot can respond to a wide range of queries, helping users learn and explore healthcare topics.
        - **Interactive Interface**: Intuitive design ensures ease of use for all users, from students to professionals.

        ### Technologies Behind MediTrain AI
        - **Streamlit**: Provides an interactive and user-friendly interface for the application.
        - **Flask**: Powers the backend for handling and processing user queries.
        - **LangChain**: Enhances AI responses by structuring context-based interactions.
        - **Medical Datasets**: Carefully curated datasets ensure accurate and reliable responses.

        ### Why Choose MediTrain AI?
        - Enhance medical training with real-time conversational AI.
        - Gain access to reliable health tips and insights.
        - Improve patient communication skills in a safe and simulated environment.
    """)
    try:
        content = importlib.import_module("content")
        if hasattr(content, "content_page"):
            content.content_page()
        else:
            st.error("The content module does not have a 'content_page' function.")
    except Exception as e:
        st.error(f"Error loading the content module: {e}")
