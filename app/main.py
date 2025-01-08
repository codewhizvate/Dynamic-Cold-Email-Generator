import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    # Enhanced Custom CSS with dynamic colors and animations
    st.markdown(
        """
        <style>
            /* Gradient Animation */
            @keyframes gradient {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }
            
            .main-title {
                font-size: 3.2em;
                font-weight: bold;
                background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
                background-size: 200% 200%;
                animation: gradient 5s ease infinite;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-align: center;
                margin-bottom: 30px;
                padding: 20px;
            }
            
            /* Button Styling */
            .stButton > button {
                background: linear-gradient(135deg, #6C63FF, #FF6584);
                color: white;
                border: none;
                border-radius: 25px;
                padding: 15px 30px;
                font-size: 1.2em;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 10px 20px rgba(108, 99, 255, 0.2);
            }
            
            .stButton > button:hover {
                transform: translateY(-5px) scale(1.02);
                box-shadow: 0 15px 30px rgba(108, 99, 255, 0.3);
                background: linear-gradient(135deg, #FF6584, #6C63FF);
            }
            
            /* Input Field Styling */
            .stTextInput > div > input {
                border: 2px solid #6C63FF;
                border-radius: 15px;
                padding: 12px 20px;
                font-size: 1.1em;
                transition: all 0.3s ease;
                background: rgba(255, 255, 255, 0.9);
            }
            
            .stTextInput > div > input:focus {
                border-color: #FF6584;
                box-shadow: 0 0 15px rgba(108, 99, 255, 0.2);
                transform: scale(1.01);
            }
            
            /* Custom Cursor */
            * {
                cursor: default;
            }
            
            .stButton > button,
            .stTextInput > div > input {
                cursor: pointer;
            }
            
            /* Expander Styling */
            .streamlit-expanderHeader {
                background: linear-gradient(90deg, #6C63FF22, #FF658422);
                border-radius: 10px;
                padding: 10px;
                transition: all 0.3s ease;
            }
            
            .streamlit-expanderHeader:hover {
                background: linear-gradient(90deg, #6C63FF44, #FF658444);
                transform: scale(1.01);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='main-title'>✨ Dynamic Email Assistant</h1>", unsafe_allow_html=True)

    # Layout using columns with adjusted ratios
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        url_input = st.text_input("🔗 Enter the Job URL:", value="https://jobs.nike.com/job/R-33460")
        submit_button = st.button("🚀 Generate Magic Email")

    if submit_button:
        with st.spinner("✨ Crafting your perfect email..."):
            try:
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)

                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)

                    with st.expander(f"📧 Generated Email for {job.get('title', 'Job')}"):
                        st.code(email, language='markdown')

            except Exception as e:
                st.error(f"⚠️ An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(
        layout="wide",
        page_title=" Dynamic Email Assistant",
        page_icon="🚀",
        initial_sidebar_state="collapsed"
    )
    create_streamlit_app(chain, portfolio, clean_text)