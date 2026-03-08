import streamlit as st
import streamlit.components.v1 as components
import os

# Ultra-clean mobile-first industrial dashboard wrapper
st.set_page_config(
    page_title="Command Center",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Force-remove all streamlit UI elements for a native app experience
st.markdown("""
    <style>
        /* Hide all Streamlit junk */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stHeader"] {display:none;}
        
        /* Remove paddings */
        .main .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
        }
        
        /* Ensure the iframe fills the viewport correctly */
        iframe {
            border: none !important;
            width: 100% !important;
            display: block;
        }
        
        /* Custom scrollbar for a premium feel */
        ::-webkit-scrollbar {
            width: 0px;
            background: transparent;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    html_path = "index.html"
    
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # We use a height that generally fits mobile viewports without vertical streamlit scrolling.
        # 95vh is used to account for mobile browser bars.
        components.html(
            html_content, 
            height=850, # Set to a height that fits most mobile screens perfectly
            scrolling=False # Let React handle internal scrolling
        )
    else:
        st.error("Build 'index.html' not found. Please upload to the root directory.")

if __name__ == "__main__":
    main()
