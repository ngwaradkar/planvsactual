import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config for mobile-first feel
st.set_page_config(
    page_title="Plan Vs Actual - Command Center",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS to remove streamlit padding and header/footer for a full-screen app feel
st.markdown("""
    <style>
        .reportview-container .main .block-container {
            padding: 0;
            max-width: 100%;
        }
        header, footer {
            visibility: hidden;
            display: none !important;
        }
        #MainMenu { 
            visibility: hidden; 
        }
        /* Mobile optimization for the component container */
        iframe {
            border: none;
            width: 100vw;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    # Path to the bundled React app
    html_path = "index.html"
    
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # Display the React App
        # height=2400 to match Mi 11i aspect ratio and prevent internal scrolling
        components.html(html_content, height=2400, scrolling=True)
    else:
        st.error("Application build not found. Please run 'npm run build' first.")

if __name__ == "__main__":
    main()
