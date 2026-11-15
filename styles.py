import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>
        /* =================================================================
           1. FONTS & TYPOGRAPHY IMPORTS
           - Lora: Elegant classic serif font for headings
           - Inter: Clean, modern sans-serif font for body text
           ================================================================= */
        @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap');

        /* =================================================================
           2. GLOBAL COLOR PALETTE TOKENS
           - Primary Theme: Deep Forest Teal (#264E49) - Rich, grounded, gender-neutral
           - Accent: Warm Bronze (#9C7A4C) - Adds warmth to borders, highlights, & hovers
           - Accent Silver: Brushed Silver (#A8B1BA / #D5DBE0) - Clean metallic trim
           - Background: Warm Parchment (#F7F3EA) & Linen (#EFE8D8) - Soft paper tone
           - Text: Deep Charcoal (#2B2D2F) - High legibility reading text
           ================================================================= */
        :root {
            --brand-primary: #264E49;        /* Deep Forest Teal */
            --brand-primary-dark: #1B3834;   /* Darker Teal for active states */
            --brand-primary-soft: rgba(38, 78, 73, 0.08); /* Light Teal tint */
            --brand-accent: #9C7A4C;         /* Warm Bronze */
            --brand-silver: #A8B1BA;         /* Brushed Silver */
            --brand-silver-light: #D5DBE0;   /* Light Silver border trim */
            --bg-parchment: #F7F3EA;       /* Main Parchment background */
            --bg-linen: #EFE8D8;           /* Warm Linen container background */
            --text-ink: #2B2D2F;           /* Primary Body Text (Deep Charcoal) */
            --text-muted: #5C6268;         /* Subtitles & Captions (Muted Slate) */
        }

        /* =================================================================
           3. MAIN APP BACKGROUND & DEFAULT BODY TEXT
           Sets the parchment background color (#F7F3EA) and base font (Inter).
           ================================================================= */
        .stApp {
            background-color: var(--bg-parchment);
            color: var(--text-ink);
            font-family: 'Inter', sans-serif;
        }

        /* =================================================================
           4. SECTION HEADINGS (H1, H2, H3, H4)
           Styles all headers with classic book serif (Lora) in Deep Teal (#264E49).
           ================================================================= */
        h1, h2, h3, h4 {
            font-family: 'Lora', serif !important;
            color: var(--brand-primary) !important;
            letter-spacing: -0.01em;
        }

        /* =================================================================
           5. SIDEBAR NAVIGATION
           Gives the sidebar a warm linen background (#EFE8D8) with silver right border.
           ================================================================= */
        [data-testid="stSidebar"] {
            background-color: var(--bg-linen);
            border-right: 1px solid var(--brand-silver);
        }
        [data-testid="stSidebar"] * {
            color: var(--text-ink) !important;
        }

        /* =================================================================
           6. HERO HEADER BOX (Top Banner "Bible Focus")
           Creates a soft gradient banner with a 6px Deep Teal (#264E49) top border
           and 3px Warm Bronze (#9C7A4C) bottom accent trim.
           ================================================================= */
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
            color: var(--brand-accent) !important; /* Subtitle in Warm Bronze (#9C7A4C) */
            font-weight: 500;
            font-size: 1.05rem;
        }

        /* =================================================================
           7. FEATURED CARDS (Daily Verse & Passage Lookup Spotlight)
           Creates white/cream elevated cards with a 6px Warm Bronze (#9C7A4C) left edge.
           ================================================================= */
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

        /* =================================================================
           8. STREAMLIT CONTAINER CARDS (st.container(border=True))
           Styles all grid cards (Directories, Challenges, Games, Calendar) with 
           a 4px Deep Teal (#264E49) top bar and subtle cream background gradient.
           ================================================================= */
        [data-testid="stVerticalBlockBorderWrapper"] > div {
            background: linear-gradient(180deg, #FFFFFF 0%, #FAF6EE 100%) !important;
            border: 1px solid var(--brand-silver) !important;
            border-top: 4px solid var(--brand-primary) !important;
            border-radius: 14px !important;
            box-shadow: 0 4px 14px rgba(38, 78, 73, 0.05) !important;
        }

        /* =================================================================
           9. ACTION BUTTONS & LINK BUTTONS
           - Default: Solid Deep Forest Teal (#264E49) with white bold text
           - Hover: Shifts to Warm Bronze (#9C7A4C)
           ================================================================= */
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

        /* =================================================================
           10. DISABLED BUTTONS ("Coming Soon" Placeholders)
           Gives non-interactive buttons a subtle silver outline (#A8B1BA)
           and soft muted background so they don't look distracting.
           ================================================================= */
        .stButton > button:disabled {
            background-color: #F4F1EA !important;
            color: #7A828A !important;
            border: 1px solid var(--brand-silver) !important;
            box-shadow: none !important;
            opacity: 0.9 !important;
        }

        /* =================================================================
           11. TOPIC PILLS ("Bible About..." Category Chips)
           - Default: White pill with silver outline & Teal text
           - Selected: Solid Deep Teal (#264E49) with white text
           ================================================================= */
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

        /* =================================================================
           12. NAVIGATION SEARCH TABS
           Underlines active tab in Warm Bronze (#9C7A4C) with Teal active text.
           ================================================================= */
        button[data-baseweb="tab"] {
            color: var(--text-muted) !important;
            font-weight: 600 !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: var(--brand-primary) !important;
            border-bottom-color: var(--brand-accent) !important;
        }

        /* =================================================================
           13. INPUT FIELDS & DROPDOWNS
           Gives search boxes and select dropdowns rounded silver borders.
           ================================================================= */
        div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
            border-radius: 10px !important;
            border-color: var(--brand-silver) !important;
            background-color: #FFFFFF !important;
        }

        /* =================================================================
           14. HORIZONTAL SECTION DIVIDERS
           Multi-color gradient line combining Silver (#A8B1BA) & Bronze (#9C7A4C).
           ================================================================= */
        hr {
            border: 0 !important;
            height: 2px !important;
            background: linear-gradient(to right, transparent, var(--brand-silver), var(--brand-accent), var(--brand-silver), transparent) !important;
            margin: 1.75rem 0 !important;
        }

        /* =================================================================
           15. INLINE HYPERLINKS
           ================================================================= */
        a {
            color: var(--brand-primary) !important;
            font-weight: 500;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
