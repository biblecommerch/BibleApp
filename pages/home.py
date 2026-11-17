import streamlit as st
import pandas as pd
import os
from datetime import datetime
from styles import apply_global_styles
from auth_helper import render_sidebar_auth

st.set_page_config(
    page_title="Bible Focus — Home",
    page_icon="📖",
    layout="centered"
)

apply_global_styles()
render_sidebar_auth()

# ==========================================
# HELPER FUNCTIONS
# ==========================================
@st.cache_data
def load_bible_data(csv_filename="KJV.csv"):
    # Check common paths and casing on Streamlit Cloud
    candidates = [
        os.path.join("data", csv_filename),
        os.path.join("data", csv_filename.lower()),
        csv_filename,
        csv_filename.lower(),
    ]
    for path in candidates:
        if os.path.exists(path):
            return pd.read_csv(path)
    return None

def get_daily_verse_index():
    return datetime.now().timetuple().tm_yday

def generate_verse_reflection(book_name: str, chap: int, v_num: int, verse_text: str) -> str:
    t = verse_text.lower()
    
    if any(w in t for w in ["rich", "gold", "silver", "bless", "blessed", "increase", "prosper", "inheritance", "land"]):
        return (
            f"In {book_name} {chap}:{v_num}, we see how God's provision and blessing unfold in the lives of His people. "
            f"True abundance isn't just about material increase—it's a reminder that everything we hold comes from God's faithful hand "
            f"and is meant to be stewarded with gratitude, humility, and generosity."
        )
    elif any(w in t for w in ["fear not", "afraid", "dismayed", "trouble", "anxious", "peace", "refuge", "shield", "strength"]):
        return (
            f"{book_name} {chap}:{v_num} speaks directly to moments when worry or uncertainty tries to take hold. "
            f"God doesn't ask you to muster up strength on your own; He invites you to anchor your heart in His steady presence."
        )
    elif any(w in t for w in ["love", "charity", "kindness", "mercy", "forgive", "compassion", "grace"]):
        return (
            f"The heart of {book_name} {chap}:{v_num} points us toward the character of God—steadfast in mercy, rich in grace, "
            f"and overflowing with love."
        )
    elif any(w in t for w in ["wisdom", "understanding", "knowledge", "teach", "counsel", "way", "path", "light", "truth"]):
        return (
            f"Scripture in {book_name} {chap}:{v_num} reminds us that true wisdom begins with seeking God's perspective above our own."
        )
    elif any(w in t for w in ["pray", "prayer", "cry", "heard", "call upon", "ask", "seek"]):
        return (
            f"{book_name} {chap}:{v_num} is an open invitation to bring every burden, question, and thank-you directly before God."
        )
    elif any(w in t for w in ["faith", "believe", "trust", "hope", "promise", "covenant", "faithful"]):
        return (
            f"In {book_name} {chap}:{v_num}, we're called to hold fast to God's promises even before we see the full picture."
        )
    elif any(w in t for w in ["sin", "repent", "cleanse", "righteous", "holy", "obey", "command", "law", "statutes"]):
        return (
            f"{book_name} {chap}:{v_num} calls us back to a life aligned with God's heart and holiness."
        )
        
    return (
        f"Every detail in {book_name} {chap}:{v_num} sits inside God's larger story of redemption and faithfulness. "
        f"Take a quiet moment to read this verse in its surrounding chapter today."
    )

# ==========================================
# HEADER SECTION
# ==========================================
st.markdown(
    """
    <div style="background-color: #2b3a2a; padding: 32px 24px; border-radius: 12px; text-align: center; border: 1px solid #4a6b4e; margin-bottom: 25px;">
        <h1 style="margin: 0 !important; color: #f4f1ea !important; font-size: 2.1em;">Welcome to Your Bible App</h1>
        <p style="margin-top: 8px !important; margin-bottom: 0 !important; color: #d5e8d6 !important; font-size: 1.05em;">
            Your daily space for scripture search, reflection, and reading plans.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# QUICK NAVIGATION SECTION
# ==========================================
st.markdown("### Where would you like to go?")

col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/bible_search.py", label="Bible Search", icon="🔍", use_container_width=True)
with col2:
    st.page_link("pages/translations.py", label="Translations", icon="⚖️", use_container_width=True)
with col3:
    st.page_link("pages/thirty_day_challenge.py", label="30 Day Challenge", icon="📅", use_container_width=True)

st.write("")

# ==========================================
# DAILY VERSE SECTION
# ==========================================
st.markdown("### ✨ Daily Verse")

kjv_master = load_bible_data("KJV.csv")

if kjv_master is not None and not kjv_master.empty:
    idx = get_daily_verse_index() % len(kjv_master)
    daily_row = kjv_master.iloc[idx]
    
    # Flexible column lookup
    cols_lower = {str(c).strip().lower(): c for c in kjv_master.columns}
    b_col = cols_lower.get("book", kjv_master.columns[0])
    c_col = cols_lower.get("chapter", kjv_master.columns[1] if len(kjv_master.columns) > 1 else kjv_master.columns[0])
    v_col = cols_lower.get("verse", cols_lower.get("v", kjv_master.columns[2] if len(kjv_master.columns) > 2 else kjv_master.columns[0]))
    t_col = cols_lower.get("text", cols_lower.get("content", cols_lower.get("verse_text", kjv_master.columns[-1])))

    book = str(daily_row[b_col])
    chapter = int(daily_row[c_col])
    verse_num = int(daily_row[v_col])
    text = str(daily_row[t_col])
else:
    # Guaranteed fallback if CSV path differs
    book, chapter, verse_num = "Psalm", 119, 105
    text = "Thy word is a lamp unto my feet, and a light unto my path."

reflection_text = generate_verse_reflection(book, chapter, verse_num, text)

st.markdown(
    f"""
    <div class="card" style="background-color: #f9f6f0; padding: 22px; border-radius: 10px; border: 1px solid #e2d9c8;">
        <p style="font-size: 1.15em; color: #2c221e !important; margin-bottom: 8px;"><b>"{text}"</b></p>
        <p style="margin-bottom: 12px; color: #5c4b37 !important; font-weight: 600;">— {book} {chapter}:{verse_num} (KJV)</p>
        <hr style="border: 0; border-top: 1px solid #e2d9c8; margin: 12px 0;">
        <p style="margin: 0; font-size: 0.95em; color: #2c221e !important; line-height: 1.5;">
            <b>Daily Reflection &amp; Encouragement:</b> {reflection_text}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# FOOTER SECTION
# ==========================================
st.markdown("---")
st.info("💡 **Tip:** Use the sidebar menu to navigate between your study tools, personal notes, and reading challenges.")
