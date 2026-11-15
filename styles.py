import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap');

        :root {
            --brand-primary: #3A4652;
            --brand-primary-dark: #28313B;
            --brand-primary-soft: rgba(58, 70, 82, 0.08);
            --brand-silver: #A8B1BA;
            --brand-silver-light: #D5DBE0;
            --bg-parchment: #FAF7F2;
            --bg-linen: #F2ECE1;
            --text-ink: #2C2F33;
            --text-muted: #626A73;
        }

        .stApp {
            background-color: var(--bg-parchment);
            color: var(--text-ink);
            font-family: 'Inter', sans-serif;
        }

        /* Headings in Deep Slate Charcoal */
        h1, h2, h3, h4 {
            font-family: 'Lora', serif !important;
            color: var(--brand-primary) !important;
            letter-spacing: -0.01em;
        }

        [data-testid="stSidebar"] {
            background-color: var(--bg-linen);
            border-right: 1px solid var(--brand-silver-light);
        }
        [data-testid="stSidebar"] * {
            color: var(--text-ink) !important;
        }

        /* Hero Header Box with Brushed Silver Top Accent */
        .header-box {
            background: linear-gradient(145deg, #FFFFFF 0%, #F5EFE6 100%);
            padding: 38px 28px;
            border-radius: 16px;
            text-align: center;
            border: 1px solid var(--brand-silver-light);
            border-top: 5px solid var(--brand-silver);
            box-shadow: 0 8px 24px rgba(44, 47, 51, 0.06);
            margin-bottom: 28px;
        }
        .header-box h1 {
            font-size: 2.4rem !important;
            margin-bottom: 6px !important;
        }
        .header-box p {
            color: var(--text-muted) !important;
            font-size: 1.05rem;
        }

        /* Content Cards with Slate Left Accent & Silver Border */
        .card {
            background-color: #FFFFFF;
            padding: 26px 28px;
            border-radius: 14px;
            border: 1px solid var(--brand-silver-light);
            border-left: 5px solid var(--brand-primary);
            box-shadow: 0 6px 18px rgba(44, 47, 51, 0.05);
            margin-bottom: 22px;
            color: var(--text-ink);
        }
        .card p {
            color: #3E444A !important;
            line-height: 1.65;
        }

        /* Bordered Containers with Brushed Silver Top Trim */
        [data-testid="stVerticalBlockBorderWrapper"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid var(--brand-silver-light) !important;
            border-top: 3px solid var(--brand-silver) !important;
            border-radius: 14px !important;
            box-shadow: 0 4px 14px rgba(44, 47, 51, 0.04) !important;
        }

        /* Buttons in Deep Slate */
        .stButton > button, .stLinkButton > a {
            background-color: #FFFFFF !important;
            color: var(--brand-primary) !important;
            border: 1.5px solid var(--brand-primary) !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
        }
        .stButton > button:hover, .stLinkButton > a:hover {
            background-color: var(--brand-primary) !important;
            color: #FFFFFF !important;
            border-color: var(--brand-primary) !important;
        }

        .stButton > button:disabled {
            background-color: #F8F8F8 !important;
            color: #8E959C !important;
            border: 1px solid var(--brand-silver-light) !important;
            opacity: 0.85 !important;
        }

        /* Topic Pills */
        [data-testid="stPills"] button {
            border-radius: 999px !important;
            border: 1px solid var(--brand-silver) !important;
            background-color: #FFFFFF !important;
            color: var(--text-ink) !important;
        }
        [data-testid="stPills"] button[aria-pressed="true"] {
            background-color: var(--brand-primary) !important;
            border-color: var(--brand-primary) !important;
            color: #FFFFFF !important;
        }

        /* Active Tab Underline */
        button[data-baseweb="tab"] {
            color: var(--text-muted) !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: var(--brand-primary) !important;
            border-bottom-color: var(--brand-primary) !important;
        }

        div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
            border-radius: 10px !important;
            border-color: var(--brand-silver) !important;
            background-color: #FFFFFF !important;
        }

        /* Silver Gradient Dividers */
        hr {
            border: 0 !important;
            height: 1px !important;
            background: linear-gradient(to right, transparent, var(--brand-silver), transparent) !important;
            margin: 1.75rem 0 !important;
        }

        a {
            color: var(--brand-primary) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
