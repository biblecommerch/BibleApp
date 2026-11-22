# ==========================================
# IMPORTS & DEPENDENCIES
# ==========================================
from datetime import datetime
from pathlib import Path
import re
import pandas as pd
import streamlit as st
from styles import apply_global_styles
from site_config import APP_NAME, APP_TAGLINE, APP_FOOTER_TAGLINE, name_to_anchor

# Import custom auth helper functions to manage sidebar login, user sessions, and database saves
from auth_helper import render_sidebar_auth, require_email_to_save, get_supabase


# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(page_title=APP_NAME, page_icon="📖", layout="centered")
apply_global_styles()


# ==========================================
# SIDEBAR ACCOUNT & SITE UPDATES MANAGER
# ==========================================
# Renders the email login/status box and the Privacy Policy link in the left sidebar on every page
try:
    render_sidebar_auth()
except Exception as e:
    st.sidebar.warning("Sidebar account panel is temporarily unavailable.")
    st.sidebar.caption(f"Sidebar notice: {e}")


# ==========================================
# LOAD BIBLE DATA & TRANSLATION MAP
# ==========================================
# Dictionary connecting user-facing dropdown labels to exact CSV filenames stored in GitHub
TRANSLATIONS = {
    "KJV (King James Version)": "KJV.csv",
    "ASV (American Standard Version)": "ASV.csv",
    "BSB (Berean Standard Bible)": "BSB.csv",
    "YLT (Young's Literal Translation)": "YLT.csv",
    "BBE (Bible in Basic English)": "BBE.csv",
    "DRC (Douay-Rheims Catholic Bible)": "DRC.csv",
}

def _resolve_data_path(csv_filename):
    """Checks current working directory first, then repository root if running from pages/."""
    local_path = Path(csv_filename)
    if local_path.exists():
        return local_path
    root_path = Path(__file__).resolve().parent.parent / csv_filename
    return root_path if root_path.exists() else local_path

@st.cache_data
def load_bible_data(csv_filename):
    """
    Loads the chosen Bible CSV file into memory once and caches it.
    Caching ensures switching translations later is instant without reloading from disk.
    """
    try:
        resolved = _resolve_data_path(csv_filename)
        loaded_df = pd.read_csv(resolved)
        loaded_df.columns = [col.strip() for col in loaded_df.columns]
        return loaded_df
    except Exception:
        return None


def _is_valid_email(email):
    return bool(email and "@" in email and "." in email.split("@")[-1])


# ==========================================
# 1. HEADER & BIBLE VERSIONS
# ==========================================
# Renders the main title header box at the top of the home page
st.markdown(
    f"""
    <div class="header-box">
        <h1 style="margin:0;">{APP_NAME}</h1>
        <p style="margin-top:5px;">{APP_TAGLINE}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Preserve the user's chosen translation across different pages using Streamlit session state
if "selected_version" not in st.session_state:
    st.session_state.selected_version = "KJV (King James Version)"

ver_col1, ver_col2, ver_col3 = st.columns([1, 2, 1])
with ver_col2:
    version = st.selectbox(
        "Select Bible Translation:",
        options=list(TRANSLATIONS.keys()),
        index=list(TRANSLATIONS.keys()).index(st.session_state.selected_version),
    )

# Save the user's latest translation selection and extract the short code (e.g., "KJV", "BSB")
st.session_state.selected_version = version
ver_code = version.split(" ")[0]

# Load only the selected translation DataFrame into memory for use across the rest of the page
df = load_bible_data(TRANSLATIONS[version])


# ==========================================
# 2. DAILY VERSE + COMMENTARY / ENCOURAGEMENT
# ==========================================
st.markdown("### ✨ Daily Verse")

if df is not None and not df.empty:
    # Uses the current day of the year (1-365) so all visitors see the same verse today,
    # automatically rendered in whichever Bible translation they currently have selected.
    day_of_year = datetime.now().timetuple().tm_yday
    verse_index = day_of_year % len(df)
    daily_row = df.iloc[verse_index]
    
    book = daily_row.get("Book", daily_row.get("book", ""))
    chapter = daily_row.get("Chapter", daily_row.get("chapter", ""))
    verse_num = daily_row.get("Verse", daily_row.get("verse", ""))
    text = daily_row.get("Text", daily_row.get("text", ""))

    st.markdown(
        f"""
        <div class="card">
            <p style="font-size: 1.15em;"><b>"{text}"</b></p>
            <p style="margin-bottom: 12px;">— {book} {chapter}:{verse_num} ({ver_code})</p>
            <hr style="border: 0; border-top: 1px solid #E2D9C8; margin: 10px 0;">
            <p style="margin: 0; font-size: 0.95em;">
                <b>Daily Reflection &amp; Encouragement:</b> Every passage of Scripture reminds us of God's faithfulness and purposeful guidance. Take a quiet moment today to reflect on how {book} {chapter}:{verse_num} speaks into your current walk, trusting that God's Word brings clarity and strength for each step ahead.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    # Fallback default card if dataset fails to load
    st.markdown(
        """
        <div class="card">
            <p style="font-size: 1.15em;"><b>"The Lord is my strength and my shield; my heart trusted in him, and I am helped."</b></p>
            <p style="margin-bottom: 12px;">— Psalm 28:7 (KJV)</p>
            <hr style="border: 0; border-top: 1px solid #E2D9C8; margin: 10px 0;">
            <p style="margin: 0; font-size: 0.95em;">
                <b>Daily Reflection &amp; Encouragement:</b> When life feels heavy, God does not ask you to carry it alone. Lean on Him as both your strength to endure and your shield to protect your peace today.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================
# 3. DUAL BIBLE SEARCH (PASSAGE + KEYWORD)
# ==========================================
st.markdown("---")
st.subheader("🔍 Bible Search")

search_tab1, search_tab2 = st.tabs([
    "📖 Passage / Verse Lookup (e.g., Romans 8:28)",
    "🔎 Keyword & Phrase Search"
])

# Tab 1: Exact Passage Lookup
with search_tab1:
    passage_input = st.text_input(
        "Enter a specific Book, Chapter, and Verse:",
        placeholder="e.g., Romans 8:28, John 3:16, Psalm 23:1...",
        key="passage_lookup",
    )
    if passage_input:
        if df is not None and not df.empty:
            match = re.match(r"^\s*([1-3]?\s*[A-Za-z]+)\s+(\d+):(\d+)\s*$", passage_input)
            book_col = "Book" if "Book" in df.columns else "book"
            chap_col = "Chapter" if "Chapter" in df.columns else "chapter"
            verse_col = "Verse" if "Verse" in df.columns else "verse"
            text_col = "Text" if "Text" in df.columns else "text"

            if match:
                b_name, c_num, v_num = match.group(1).strip(), int(match.group(2)), int(match.group(3))
                found = df[
                    (df[book_col].astype(str).str.lower() == b_name.lower()) &
                    (df[chap_col].astype(int) == c_num) &
                    (df[verse_col].astype(int) == v_num)
                ]
                if not found.empty:
                    row = found.iloc[0]
                    st.markdown(
                        f"""
                        <div class="card">
                            <p style="font-size: 1.1em;"><b>"{row[text_col]}"</b></p>
                            <p style="margin: 0;">— {row[book_col]} {row[chap_col]}:{row[verse_col]} ({ver_code})</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning(f"Could not find '{passage_input}' in {ver_code}. Check book spelling and verse numbers.")
            else:
                st.info("Tip: Use the format **Book Chapter:Verse** (for example: `Romans 8:28`).")
        else:
            st.error(f"Bible dataset ({TRANSLATIONS[version]}) could not be loaded.")

# Tab 2: Keyword & Phrase Search Across Active Translation
with search_tab2:
    keyword_input = st.text_input(
        f"Search by word or phrase across the entire {ver_code} Bible:",
        placeholder="e.g., all things work together, peace, grace...",
        key="keyword_lookup",
    )
    if keyword_input:
        if df is not None and not df.empty:
            text_col = "Text" if "Text" in df.columns else "text"
            results = df[df[text_col].astype(str).str.contains(keyword_input, case=False, na=False)]
            if not results.empty:
                max_rows = 20
                st.success(f"Found {len(results)} matching verse(s) in {ver_code}:")
                if len(results) > max_rows:
                    st.caption(f"Showing the first {max_rows} of {len(results)} matching verses in **{ver_code}**.")
                st.dataframe(results.head(max_rows), use_container_width=True)
            else:
                st.warning(f"No verses found matching '{keyword_input}' in {ver_code}.")
        else:
            st.error(f"Bible dataset ({TRANSLATIONS[version]}) could not be loaded.")


# ==========================================
# 4. OLD & NEW TESTAMENT DIRECTORIES
# ==========================================
st.markdown("---")
st.subheader("📚 Scripture Directories")

dir_col1, dir_col2 = st.columns(2)
with dir_col1:
    with st.container(border=True):
        st.markdown("### 📜 Old Testament Directory")
        st.write("Browse all 39 books from Genesis to Malachi by Law, History, Poetry, and Prophets.")
        st.button("Browse Old Testament (Coming Soon)", disabled=True, use_container_width=True)

with dir_col2:
    with st.container(border=True):
        st.markdown("### ✝️ New Testament Directory")
        st.write("Browse all 27 books from Matthew to Revelation by Gospels, History, Epistles, and Prophecy.")
        st.button("Browse New Testament (Coming Soon)", disabled=True, use_container_width=True)


# ==========================================
# 5. BIBLE ABOUT... (POPULAR TOPIC PILLS)
# ==========================================
st.markdown("---")
st.subheader("💬 Bible About...")
st.write("Tap a topic bubble below to explore top verses:")

topics = [
    "Anxiety & Worry", "Faith", "Love", "Healing", "Strength",
    "Forgiveness", "Peace", "Marriage & Family", "Hope", "Prayer",
]
selected_topic = st.pills("Popular Topics", topics, selection_mode="single")
if selected_topic:
    st.info(f"**Top Verses About {selected_topic}:** *(Placeholder — curated {selected_topic} verse collection coming soon!)*")


# ==========================================
# 6. POPULAR VERSES (QUICK CARDS)
# ==========================================
st.markdown("---")
st.subheader("📌 Popular Verses")

def get_verse_text(book_name, chap_num, verse_num):
    """Helper function to fetch a specific verse's text cleanly from the active DataFrame."""
    if df is None or df.empty:
        return ""
    b_col = "Book" if "Book" in df.columns else "book"
    c_col = "Chapter" if "Chapter" in df.columns else "chapter"
    v_col = "Verse" if "Verse" in df.columns else "verse"
    t_col = "Text" if "Text" in df.columns else "text"

    hit = df[
        (df[b_col].astype(str).str.lower().isin([book_name.lower(), book_name.lower() + "s"])) &
        (df[c_col].astype(int) == chap_num) &
        (df[v_col].astype(int) == verse_num)
    ]
    return hit.iloc[0][t_col] if not hit.empty else ""

with st.container(border=True):
    pop_col1, pop_col2 = st.columns(2)
    with pop_col1:
        st.markdown(
            f"""
- **Romans 8:28** — *{get_verse_text("Romans", 8, 28)}*
- **John 3:16** — *{get_verse_text("John", 3, 16)}*
- **Philippians 4:13** — *{get_verse_text("Philippians", 4, 13)}*
            """
        )
    with pop_col2:
        st.markdown(
            f"""
- **Jeremiah 29:11** — *{get_verse_text("Jeremiah", 29, 11)}*
- **Psalm 23:1** — *{get_verse_text("Psalm", 23, 1)}*
- **Proverbs 3:5** — *{get_verse_text("Proverbs", 3, 5)}*
            """
        )
st.button("Explore Full Popular Verses Collection (Coming Soon)", disabled=True, use_container_width=True)


# ==========================================
# 7. 30-DAY BIBLE CHALLENGES (3 PERSPECTIVES)
# ==========================================
st.markdown("---")
st.subheader("📅 30-Day Bible Challenges")
st.write("Choose a 30-day reading path tailored to your spiritual focus:")

chal_col1, chal_col2, chal_col3 = st.columns(3)
with chal_col1:
    with st.container(border=True):
        st.markdown("#### 🌱 Track 1: Foundations")
        st.write("Essential KJV passages covering creation, faith, salvation, and daily Christian living.")
        if st.button("Start Foundations", key="chal_1", use_container_width=True):
            st.switch_page("pages/thirty_day_challenge.py")

with chal_col2:
    with st.container(border=True):
        st.markdown("#### 🕊️ Track 2: Peace & Wisdom")
        st.write("30 days walking through Psalms and Proverbs for comfort, clarity, and overcoming worry.")
        st.button("Coming Soon", disabled=True, key="chal_2", use_container_width=True)

with chal_col3:
    with st.container(border=True):
        st.markdown("#### ✝️ Track 3: Life of Christ")
        st.write("Follow the teachings, parables, and miracles of Jesus through the four Gospels.")
        st.button("Coming Soon", disabled=True, key="chal_3", use_container_width=True)


# ==========================================
# 8. JUST FOR FUN — BIBLE GAMES
# ==========================================
st.markdown("---")
st.subheader("🎮 Just for Fun — Bible Games")
st.write("Sharpen your Scripture memory with quick, family-friendly Bible games:")

g_col1, g_col2, g_col3 = st.columns(3)
with g_col1:
    with st.container(border=True):
        st.markdown("#### 🗣️ Who Said It?")
        st.write("Read a famous KJV quote and guess which biblical figure spoke it.")
        st.button("Play Soon", disabled=True, key="g_who", use_container_width=True)
with g_col2:
    with st.container(border=True):
        st.markdown("#### 🔀 Verse Scramble")
        st.write("Unscramble key words from well-known Scriptures against the clock.")
        st.button("Play Soon", disabled=True, key="g_scr", use_container_width=True)
with g_col3:
    with st.container(border=True):
        st.markdown("#### ❓ Bible Trivia")
        st.write("Multiple-choice trivia spanning Old & New Testament stories.")
        st.button("Play Soon", disabled=True, key="g_tri", use_container_width=True)

g_col4, g_col5 = st.columns(2)
with g_col4:
    with st.container(border=True):
        st.markdown("#### ✍️ Fill in the Blank")
        st.write("Complete the missing words in classic memory verses.")
        st.button("Play Soon", disabled=True, key="g_fil", use_container_width=True)
with g_col5:
    with st.container(border=True):
        st.markdown("#### ⚡ Old or New Testament?")
        st.write("Fast-paced challenge: sort books, prophets, and events into the right Testament.")
        st.button("Play Soon", disabled=True, key="g_ont", use_container_width=True)


# ==========================================
# 9. DEDICATED CALENDAR & HOLY DAYS
# ==========================================
st.markdown("---")
st.subheader("🗓️ Biblical Calendar & Holy Days")

with st.container(border=True):
    cal_col1, cal_col2 = st.columns([2, 1])
    with cal_col1:
        st.markdown("### Feasts, Seasons & Christian Calendar")
        st.write(
            "Explore Old Testament appointed feasts (Passover, Pentecost, Tabernacles), "
            "Christian church seasons, and historical dates tied to Scripture."
        )
    with cal_col2:
        st.markdown("**Upcoming Highlights:**")
        st.caption("• Advent & Nativity Readings\n• Biblical Feast Guide\n• Yearly Reading Milestones")
        st.button("Open Full Calendar (Soon)", disabled=True, use_container_width=True)


# ==========================================
# 10. HISTORICAL BIBLE MAPS SPOTLIGHT
# ==========================================
st.markdown("---")
st.subheader("🗺️ Historical Bible Maps")
st.write("Visualize the lands, journeys, and kingdoms of Scripture:")

map_choice = st.selectbox(
    "Select a Historical Map Preview:",
    [
        "The Journeys of the Apostle Paul",
        "The Twelve Tribes of Israel",
        "The Exodus Route from Egypt to Canaan",
    ],
)

map_urls = {
    "The Journeys of the Apostle Paul": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Map_of_Paul%27s_missionary_journeys-en.svg/1024px-Map_of_Paul%27s_missionary_journeys-en.svg.png",
        "Trace Paul's missionary routes across Asia Minor, Greece, and Rome (Acts 13–28).",
    ),
    "The Twelve Tribes of Israel": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/12_Tribes_of_Israel_Map.svg/800px-12_Tribes_of_Israel_Map.svg.png",
        "Allotment of the Promised Land among the Twelve Tribes of Israel (Joshua 13–21).",
    ),
    "The Exodus Route from Egypt to Canaan": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Map_of_the_Exodus.svg/1024px-Map_of_the_Exodus.svg.png",
        "Traditional route of the Israelites from Goshen through Sinai toward Canaan.",
    ),
}

with st.container(border=True):
    img_url, img_caption = map_urls[map_choice]
    st.image(img_url, caption=img_caption, use_container_width=True)
    st.button("Explore Full Interactive Atlas (Coming Soon)", disabled=True, use_container_width=True)


# ==========================================
# 11. TOP BLOGS & EMAIL NEWSLETTER
# ==========================================
st.markdown("---")
blog_col, news_col = st.columns(2)

# Left Column: Blog Link
with blog_col:
    with st.container(border=True):
        st.markdown("### ✍️ Top Blogs")
        st.write("Read featured articles, devotions, and reader discussions on Bible Com Blog.")
        st.link_button("Visit Bible Com Blog", "https://www.biblecomblog.com", use_container_width=True)

# Right Column: Email Newsletter Signup (Supabase Connected)
with news_col:
    with st.container(border=True):
        st.markdown("### ✉️ Join Email Newsletter")
        st.write("Stay updated with daily verses, new studies, and site additions.")

        newsletter_email = st.text_input(
            "Your Email Address:",
            placeholder="you@example.com",
            label_visibility="collapsed",
            key="home_newsletter_input",
        )

        if st.button("Stay Updated", use_container_width=True, key="home_newsletter_submit"):
            cleaned_email = newsletter_email.strip().lower()
            if _is_valid_email(cleaned_email):
                try:
                    db = get_supabase()
                    db.table("users").upsert({
                        "email": cleaned_email,
                        "site_updates": True,
                    }).execute()
                    st.session_state["user_email"] = cleaned_email
                    st.success("🎉 You're on the list! We'll notify you when new features drop.")
                except Exception:
                    st.error("Could not save email. Please try again.")
            else:
                st.warning("Please enter a valid email address.")


# ==========================================
# 12. EXPLORE MORE APP PAGES
# ==========================================
explore_heading = f"Explore More {APP_NAME} Pages"
explore_anchor = name_to_anchor(explore_heading)
home_anchor = name_to_anchor(APP_NAME)

st.markdown("---")
st.subheader(f"🧭 {explore_heading}")
st.write("Dedicated tools and sections currently in development:")

p_col1, p_col2, p_col3 = st.columns(3)
with p_col1:
    with st.container(border=True):
        st.markdown("#### 🔬 Bible Research")
        st.caption("Bible Study • Reading Plans • Scripture AI & Commentary DB • Timelines")
        st.button("Coming Soon", disabled=True, key="p_res", use_container_width=True)
with p_col2:
    with st.container(border=True):
        st.markdown("#### 🎧 Listen to the Bible")
        st.caption("Audio Bible Player • Chapter Narration • Background Study Listening")
        st.button("Coming Soon", disabled=True, key="p_lis", use_container_width=True)
with p_col3:
    with st.container(border=True):
        st.markdown("#### 🙏 Prayer Page")
        st.caption("Guided Prayers • Submit a Prayer Request • Prayer Ideas & Prompts")
        st.button("Coming Soon", disabled=True, key="p_pray", use_container_width=True)

p_col4, p_col5 = st.columns(2)
with p_col4:
    with st.container(border=True):
        st.markdown("#### ❤️ My Mission")
        st.caption(f"Our Vision • Why {APP_NAME} Is Free • Support & Donations")
        st.button("Coming Soon", disabled=True, key="p_mis", use_container_width=True)
with p_col5:
    with st.container(border=True):
        st.markdown("#### 📬 Contact Me")
        st.caption("Social Media Links • Questions • Feedback & Contact Form")
        st.button("Coming Soon", disabled=True, key="p_con", use_container_width=True)


# ==========================================
# 13. SUPPORT THE PROJECT: SHOP MEL'S GOODS
# ==========================================
st.markdown("---")
st.subheader(f"🛍️ Support {APP_NAME} — Shop Mel's Goods")
with st.container(border=True):
    st.markdown("### Christian Tees & Faith-Inspired Finds")
    st.write(
        f"Every purchase from Mel's Goods helps keep {APP_NAME} free and growing. "
        "Browse our collection of Christian T-shirts and unique goods directly in our store:"
    )
    st.link_button(
        "Shop Christian Tees on eBay",
        "https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=mels_goods&store_name=shopmelsgoods&_oac=1&store_cat=49634617018",
        use_container_width=False,
    )


# ==========================================
# 14. SITE FOOTER
# ==========================================
st.markdown("---")

# Renders the centered HTML footer block (un-indented to ensure Markdown renders HTML tags cleanly)
st.markdown(
    f"""<div style="text-align: center; padding: 1.5rem 0 2rem 0; font-size: 0.9rem; opacity: 0.85;">
<p style="margin-bottom: 0.5rem;">
<strong>{APP_NAME}</strong> &nbsp;|&nbsp;
<a href="{home_anchor}" style="text-decoration: none;">Home</a> &nbsp;•&nbsp;
<a href="#bible-search" style="text-decoration: none;">Bible Search</a> &nbsp;•&nbsp;
<a href="{explore_anchor}" style="text-decoration: none;">Research &amp; Study</a> &nbsp;•&nbsp;
<a href="https://www.biblecomblog.com" target="_blank" style="text-decoration: none;">Blog</a> &nbsp;•&nbsp;
<a href="{explore_anchor}" style="text-decoration: none;">Prayer</a> &nbsp;•&nbsp;
<a href="{explore_anchor}" style="text-decoration: none;">My Mission</a> &nbsp;•&nbsp;
<a href="{explore_anchor}" style="text-decoration: none;">Contact</a>
</p>
<p style="margin-bottom: 0.5rem; font-size: 0.85rem;">
{APP_FOOTER_TAGLINE} — Scripture quotations are from the {version} (Public Domain).
</p>
<p style="margin-bottom: 0.5rem; font-size: 0.85rem;">
<a href="/privacy" target="_self" style="text-decoration: none;">Privacy Policy</a> &nbsp;|&nbsp;
<a href="{explore_anchor}" style="text-decoration: none;">Terms of Use</a> &nbsp;|&nbsp;
<a href="https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=mels_goods&store_name=shopmelsgoods&_oac=1&store_cat=49634617018" target="_blank" style="text-decoration: none;">Support via Mel's Goods</a>
</p>
<p style="margin: 0; font-size: 0.8rem; opacity: 0.7;">
© 2026 {APP_NAME}. All rights reserved.
</p>
</div>""",
    unsafe_allow_html=True,
)
