import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>
        /* Main App Background & Text */
        .stApp {
            background-color: #0F1610;
            color: #F5F3EF;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #0F1610;
            border-right: 1px solid #2B3A2A;
        }
        [data-testid="stSidebar"] nav {
            background-color: #0F1610;
        }
        
        /* Header Box */
        .header-box {
            background: linear-gradient(135deg, #1B261C 0%, #2B3A2A 100%);
            padding: 35px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #4A6B4E;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            margin-bottom: 25px;
        }
        
        /* Content Cards */
        .card {
            background-color: #1B261C;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #2B3A2A;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        
        /* Custom Buttons */
        .custom-btn {
            background-color: #4A6B4E;
            color: #F5F3EF;
            padding: 10px 22px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )
