import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>
        /* Import Classic Serif & Clean Sans-Serif Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,700;1,400&family=Inter:wght@400;500;600&display=swap');

        /* Main App Background & Default Text */
        .stApp {
            background-color: #FAF7F2;
            color: #2C2A29;
            font-family: 'Inter', sans-serif;
        }
        
        /* Headings in Classic Book Serif */
        h1, h2, h3 {
            font-family: 'Lora', serif !important;
            color: #1E3A5F !important;
        }

        /* Sidebar Styling (High Contrast & Warm Linen) */
        [data-testid="stSidebar"] {
            background-color: #F2ECE1;
            border-right: 1px solid #E2D9C8;
        }
        [data-testid="stSidebar"] * {
            color: #2C2A29 !important;
        }
        
        /* Header Box */
        .header-box {
            background: linear-gradient(135deg, #FFFFFF 0%, #F5EFE6 100%);
            padding: 35px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #E2D9C8;
            border-top: 4px solid #B8860B;
            box-shadow: 0 4px 15px rgba(44, 42, 41, 0.06);
            margin-bottom: 25px;
        }
        .header-box p {
            color: #6E655F !important;
        }
        
        /* Content Cards */
        .card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #E5DEC9;
            box-shadow: 0 4px 12px rgba(44, 42, 41, 0.05);
            margin-bottom: 20px;
            color: #2C2A29;
        }
        .card p {
            color: #4A4542 !important;
        }

        /* Style the inline buttons inside your cards */
        .card button {
            background-color: #1E3A5F !important;
            color: #FFFFFF !important;
            border-radius: 6px !important;
            padding: 10px 22px !important;
            transition: background-color 0.2s ease;
        }
        .card button:hover {
            background-color: #2B5284 !important;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )
