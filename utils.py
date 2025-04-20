import streamlit as st

def configure_page():
    st.set_page_config(
        page_title="Home",
        page_icon="🛒",
        layout="wide",
        initial_sidebar_state="expanded"
    )