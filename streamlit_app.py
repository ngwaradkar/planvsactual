import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Command Center",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stHeader"] {display:none;}
        
        /* Remove body scrolling */
        body {
            overflow: hidden !important;
            margin: 0;
            padding: 0;
        }
        
        .main .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
        }
        
        /* Ensure the iframe fills the viewport exactly like a native app */
        iframe {
            border: none !important;
            width: 100vw !important;
            height: 100vh !important;
            display: block !important;
            position: fixed !important;
            top: 0;
            left: 0;
            z-index: 999999;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    html_path = "index.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        components.html(
            html_content, 
            height=1000, # A dummy number since CSS overrides it completely
            scrolling=False
        )
    else:
        st.error("Build 'index.html' not found.")

if __name__ == "__main__":
    main()
