import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>
        /* Import Classic Serif & Clean Sans-Serif Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap');

        /* Root Theme Tokens: Dusty Mauve-Rose & Brushed Silver */
        :root {
            --brand-mauve: #9a6a70;
            --brand-mauve-dark: #7d5358;
            --brand-mauve-soft: rgba(154, 106, 112, 0.10);
            --brand-silver: #B8BFC6;
            --brand-silver-light: #D5DBE0;
            --bg-parchment: #FAF7F2;
            --bg-linen: #F2ECE1;
            --text-ink: #2C2A29;
            --text-muted: #6E655F;
        }

        /* Main App Background & Default Text */
        .stApp {
            background-color: var(--bg-parchment);
            color: var(--text-ink);
            font-family: 'Inter', sans-serif;
        }

        /* Headings in Classic Book Serif with Mauve Accent */
        h1, h2, h3, h4 {
            font-family: 'Lora', serif !important;
            color: var(--brand-mauve) !important;
            letter-spacing: -0.01em;
        }

        /* Sidebar Styling (High Contrast & Warm Linen with Silver Trim) */
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
            box-shadow: 0 8px 24px rgba(44, 42, 41, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.9);
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

        /* Elevated Content Cards (Daily Verse & Passage Lookup) */
        .card {
            background-color: #FFFFFF;
            padding: 26px 28px;
            border-radius: 14px;
            border: 1px solid var(--brand-silver-light);
            border-left: 5px solid var(--brand-mauve);
            box-shadow: 0 6px 18px rgba(44, 42, 41, 0.05);
            margin-bottom: 22px;
            color: var(--text-ink);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 26px rgba(154, 106, 112, 0.12);
        }
        .card p {
            color: #4A4542 !important;
            line-height: 1.65;
        }

        /* Streamlit Native Bordered Containers (st.container(border=True)) */
        [data-testid="stVerticalBlockBorderWrapper"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid var(--brand-silver-light) !important;
            border-top: 3px solid var(--brand-silver) !important;
            border-radius: 14px !important;
            box-shadow: 0 4px 14px rgba(44, 42, 41, 0.04) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }
        [data-testid="stVerticalBlockBorderWrapper"] > div:hover {
            transform: translateY(-2px);
            border-color: var(--brand-mauve) !important;
            box-shadow: 0 8px 20px rgba(154, 106, 112, 0.12) !important;
        }

        /* Primary & Secondary Streamlit Buttons + Link Buttons */
        .stButton > button, .stLinkButton > a, .card button {
            background-color: #FFFFFF !important;
            color: var(--brand-mauve) !important;
            border: 1.5px solid var(--brand-mauve) !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.25rem !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 2px 6px rgba(154, 106, 112, 0.08) !important;
        }
        .stButton > button:hover, .stLinkButton > a:hover, .card button:hover {
            background-color: var(--brand-mauve) !important;
            color: #FFFFFF !important;
            border-color: var(--brand-mauve) !important;
            box-shadow: 0 4px 12px rgba(154, 106, 112, 0.24) !important;
        }

        /* Disabled "Coming Soon" Buttons (Clean Brushed Silver Look) */
        .stButton > button:disabled {
            background-color: #F8F8F8 !important;
            color: #8E959C !important;
            border: 1px solid var(--brand-silver-light) !important;
            box-shadow: none !important;
            opacity: 0.85 !important;
        }

        /* Topic Pills ("Bible About...") */
        [data-testid="stPills"] button {
            border-radius: 999px !important;
            border: 1px solid var(--brand-silver) !important;
            background-color: #FFFFFF !important;
            color: var(--text-ink) !important;
            transition: all 0.18s ease !important;
        }
        [data-testid="stPills"] button:hover {
            border-color: var(--brand-mauve
