import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap');

        :root {
            --brand-primary: #264E49;
            --brand-primary-dark: #1B3834;
            --brand-primary-soft: rgba(38, 78, 73, 0.08);
            --brand-accent: #9C7A4C;
            --brand-silver: #A8B1BA;
            --brand-silver-light: #D5DBE0;
            --bg-parchment: #F7F3EA;
            --bg-linen: #EFE8D8;
            --text-ink: #2B2D2F;
            --text-muted: #5C6268;
        }

        .stApp {
            background-color: var(--bg-parchment);
            color: var(--text-ink);
            font-family: 'Inter', sans-serif;
        }

        /* Headings in Deep Forest Teal */
        h1, h2, h3, h4 {
            font-family: 'Lora', serif !important;
            color: var(--brand-primary) !important;
            letter-spacing: -0.01em;
        }

        [data-testid="stSidebar"] {
            background-color: var(--bg-linen);
            border-right: 1px solid var(--brand-silver);
        }
        [data-testid="stSidebar"] * {
            color: var(--text-ink) !important;
        }

        /* Hero Header Box with Warm Bronze & Silver Accent */
        .header-box {
            background: linear-gradient(135deg, #FFFFFF 0%, #EFE8D8 100%);
            padding: 38px 28px;
            border-radius: 16px;
            text-align: center;
            border: 1px solid var(--brand-silver);
            border-top: 6px solid var(--brand-primary);
            border-bottom: 3px solid var(--brand-accent);
            box-shadow: 0 8px 24px rgba(38, 78, 73, 0.08);
            margin-bottom: 28px;
        }
        .header-box h1 {
            font-size: 2.5rem !important;
            margin-bottom: 6px !important;
        }
        .header-box p {
            color: var(--brand-accent) !important;
            font-weight: 500;
            font-size: 1.05rem;
        }

        /* Content Cards (Daily Verse & Passage Lookup) */
        .card {
            background: linear-gradient(180deg, #FFFFFF 0%, #FCF9F2 100%);
            padding: 26px 28px;
            border-radius: 14px;
            border: 1px solid var(--brand-silver);
            border-left: 6px solid var(--brand-accent);
            box-shadow: 0 6px 18px rgba(38, 78, 73, 0.06);
            margin-bottom: 22px;
            color: var(--text-ink);
        }
        .card p {
            color: #363A3D !important;
            line-height: 1.65;
        }

        /* Bordered Containers with Teal Top Trim & Warm Cream Tint */
        [data-testid="stVerticalBlockBorderWrapper"] > div {
            background: linear-gradient(180deg, #FFFFFF 0%, #FAF6EE 100%) !important;
            border: 1px solid var(--brand-silver) !important;
            border-top: 4px solid var(--brand-primary) !important;
            border-radius: 14px !important;
            box-shadow: 0 4px 14px rgba(38, 78, 73, 0.05) !important;
        }

        /* Buttons in Deep Teal with Warm Bronze Hover */
        .stButton > button, .stLinkButton > a {
            background-color: var(--brand-primary) !important;
            color: #FFFFFF !important;
            border: 1.5px solid var(--brand-primary) !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            box-shadow: 0 3px 8px rgba(38, 78, 73, 0.16) !important;
        }
        .stButton > button:hover, .stLinkButton > a:hover {
            background-color: var(--brand-accent) !important;
            color: #FFFFFF !important;
            border-color: var(--brand-accent) !important;
        }

        /* Disabled "Coming Soon" Buttons (Clean Silver Outline) */
        .stButton > button:disabled {
            background-color: #F4F1EA !important;
            color: #7A828A !important;
            border: 1px solid var(--brand-silver) !important;
            box-shadow: none !important;
            opacity: 0.9 !important;
        }

        /* Topic Pills */
        [data-testid="stPills"] button {
            border-radius: 999px !important;
            border: 1.5px solid var(--brand-silver) !important;
            background-color: #FFFFFF !important;
            color: var(--brand-primary) !important;
            font-weight: 500 !important;
        }
        [data-testid="stPills"] button:hover {
            border-color: var(--brand-accent) !important;
            color: var(--brand-accent) !important;
        }
        [data-testid="stPills"] button[aria-pressed="true"] {
            background-color: var(--brand-primary) !important;
            border-color: var(--brand-primary) !important;
            color: #FFFFFF !important;
        }

        /* Active Tab Underline in Warm Bronze */
        button[data-baseweb="tab"] {
            color: var(--text-muted) !important;
            font-weight: 600 !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: var(--brand-primary) !important;
            border-bottom-color: var(--brand-accent) !important;
        }

        div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
            border-radius: 10px !important;
            border-color: var(--brand-silver) !important;
            background-color: #FFFFFF !important;
        }

        /* Bronze & Silver Gradient Dividers */
        hr {
            border: 0 !important;
            height: 2px !important;
            background: linear-gradient(to right, transparent, var(--brand-silver), var(--brand-accent), var(--brand-silver), transparent) !important;
            margin: 1.75rem 0 !important;
        }

        a {
            color: var(--brand-primary) !important;
            font-weight: 500;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
