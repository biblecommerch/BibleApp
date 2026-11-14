import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="30 Day Bible Challenge", page_icon="📅", layout="centered"
)

# --- CUSTOM THEME STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1b261c;
        color: #f4f1ea;
    }
    .challenge-header {
        background-color: #2b3a2a;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #4a6b4e;
        margin-bottom: 25px;
    }
    .card {
        background-color: #2b3a2a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #4a6b4e;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# --- LOAD BIBLE DATA FOR DROPDOWN READING ---
@st.cache_data
def load_bible_data():
    try:
        return pd.read_csv("KJV.csv")
    except Exception:
        return None


df = load_bible_data()

# --- HEADER & THEME PLAN ---
st.markdown(
    """
    <div class="challenge-header">
        <h1 style="margin:0;">30 Day Bible Challenge</h1>
        <p style="margin-top:5px; color: #b7d5b8;">Build a daily habit of reading God's Word, one day at a time.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- THE PLAN OVERVIEW ---
st.markdown(
    """
<div class="card">
    <h3 style="margin-top:0; color:#b7d5b8;">📖 About This 30-Day Journey</h3>
    <p>Why do these 30 verses go together? This plan is carefully structured around four key pillars of Christian faith and daily walk:</p>
    <ul>
        <li><b>Days 1–7: Foundations of Faith & Creation</b> — Establishing where we came from and anchoring our trust in God as our protector and shepherd.</li>
        <li><b>Days 8–14: The Promised Savior & Life of Christ</b> — Following the prophecy, birth, and teachings of Jesus to understand His heart and love.</li>
        <li><b>Days 15–21: Grace, Forgiveness, & New Life</b> — Exploring what it means to be a new creation through grace, walking in the Spirit, and loving one another.</li>
        <li><b>Days 22–30: Strength, Peace, & Endurance</b> — Equipping ourselves with the armor of God, standing strong in trials, and living with eternal hope.</li>
    </ul>
    <p style="margin-bottom:0; font-size: 0.9em; color: #b7d5b8;">Check off each day as you go, and click the dropdown under any day to read the scripture online instantly!</p>
</div>
""",
    unsafe_allow_html=True,
)

# --- 30 DAY CHALLENGE DATA ---
challenge_days = [
    {
        "day": 1,
        "topic": "Creation & Beginnings",
        "verse": "Genesis 1:1-3",
        "search_book": "Genesis",
        "chapter": 1,
    },
    {
        "day": 2,
        "topic": "The Fall & Promise",
        "verse": "Genesis 3:15",
        "search_book": "Genesis",
        "chapter": 3,
    },
    {
        "day": 3,
        "topic": "Faith of Abraham",
        "verse": "Genesis 12:1-3",
        "search_book": "Genesis",
        "chapter": 12,
    },
    {
        "day": 4,
        "topic": "The Lord is My Shepherd",
        "verse": "Psalm 23",
        "search_book": "Psalms",
        "chapter": 23,
    },
    {
        "day": 5,
        "topic": "Trust in the Lord",
        "verse": "Proverbs 3:5-6",
        "search_book": "Proverbs",
        "chapter": 3,
    },
    {
        "day": 6,
        "topic": "Awaiting the Savior",
        "verse": "Isaiah 9:6",
        "search_book": "Isaiah",
        "chapter": 9,
    },
    {
        "day": 7,
        "topic": "The Birth of Jesus",
        "verse": "Luke 2:1-14",
        "search_book": "Luke",
        "chapter": 2,
    },
    {
        "day": 8,
        "topic": "The Sermon on the Mount",
        "verse": "Matthew 5:1-12",
        "search_book": "Matthew",
        "chapter": 5,
    },
    {
        "day": 9,
        "topic": "The Lord's Prayer",
        "verse": "Matthew 6:9-13",
        "search_book": "Matthew",
        "chapter": 6,
    },
    {
        "day": 10,
        "topic": "Seeking First His Kingdom",
        "verse": "Matthew 6:33",
        "search_book": "Matthew",
        "chapter": 6,
    },
    {
        "day": 11,
        "topic": "The Good Samaritan",
        "verse": "Luke 10:25-37",
        "search_book": "Luke",
        "chapter": 10,
    },
    {
        "day": 12,
        "topic": "The Prodigal Son",
        "verse": "Luke 15:11-32",
        "search_book": "Luke",
        "chapter": 15,
    },
    {
        "day": 13,
        "topic": "God's Great Love",
        "verse": "John 3:16-17",
        "search_book": "John",
        "chapter": 3,
    },
    {
        "day": 14,
        "topic": "The Bread of Life",
        "verse": "John 6:35",
        "search_book": "John",
        "chapter": 6,
    },
    {
        "day": 15,
        "topic": "The True Vine",
        "verse": "John 15:1-8",
        "search_book": "John",
        "chapter": 15,
    },
    {
        "day": 16,
        "topic": "The Fruit of the Spirit",
        "verse": "Galatians 5:22-23",
        "search_book": "Galatians",
        "chapter": 5,
    },
    {
        "day": 17,
        "topic": "Faith Definition",
        "verse": "Hebrews 11:1-3",
        "search_book": "Hebrews",
        "chapter": 11,
    },
    {
        "day": 18,
        "topic": "Armor of God",
        "verse": "Ephesians 6:10-18",
        "search_book": "Ephesians",
        "chapter": 6,
    },
    {
        "day": 19,
        "topic": "Love is Patient",
        "verse": "1 Corinthians 13:4-7",
        "search_book": "1 Corinthians",
        "chapter": 13,
    },
    {
        "day": 20,
        "topic": "Peace That Passes Understanding",
        "verse": "Philippians 4:6-7",
        "search_book": "Philippians",
        "chapter": 4,
    },
    {
        "day": 21,
        "topic": "Strength in Weakness",
        "verse": "Philippians 4:13",
        "search_book": "Philippians",
        "chapter": 4,
    },
    {
        "day": 22,
        "topic": "New Creation",
        "verse": "2 Corinthians 5:17",
        "search_book": "2 Corinthians",
        "chapter": 5,
    },
    {
        "day": 23,
        "topic": "Saved by Grace",
        "verse": "Ephesians 2:8-9",
        "search_book": "Ephesians",
        "chapter": 2,
    },
    {
        "day": 24,
        "topic": "The Word of God",
        "verse": "Hebrews 4:12",
        "search_book": "Hebrews",
        "chapter": 4,
    },
    {
        "day": 25,
        "topic": "Drawing Near to God",
        "verse": "James 4:8",
        "search_book": "James",
        "chapter": 4,
    },
    {
        "day": 26,
        "topic": "A Chosen Generation",
        "verse": "1 Peter 2:9",
        "search_book": "1 Peter",
        "chapter": 2,
    },
    {
        "day": 27,
        "topic": "Walking in the Light",
        "verse": "1 John 1:5-7",
        "search_book": "1 John",
        "chapter": 1,
    },
    {
        "day": 28,
        "topic": "God is Love",
        "verse": "1 John 4:7-12",
        "search_book": "1 John",
        "chapter": 4,
    },
    {
        "day": 29,
        "topic": "The Alpha and Omega",
        "verse": "Revelation 21:1-6",
        "search_book": "Revelation",
        "chapter": 21,
    },
    {
        "day": 30,
        "topic": "Final Benediction",
        "verse": "Revelation 22:20-21",
        "search_book": "Revelation",
        "chapter": 22,
    },
]

# --- INITIALIZE SESSION STATE ---
if "completed_days" not in st.session_state:
    st.session_state.completed_days = {i: False for i in range(1, 31)}

# --- PROGRESS BAR TRACKING ---
completed_count = sum(st.session_state.completed_days.values())
progress_percent = completed_count / 30

st.subheader(f"Your Progress: {completed_count} / 30 Days Completed")
st.progress(progress_percent)

if completed_count == 30:
    st.balloons()
    st.success(
        "🎉 **Praise God! You have completed the 30 Day Bible Challenge!**"
    )

st.markdown("---")
st.markdown("### Daily Reading Checklist & Reader")
st.write(
    "Check off each day as you read, and expand the box below any day to read the scripture right online:"
)

# --- DISPLAY CHECKLIST WITH EXPANDABLE VERSE READERS ---
for item in challenge_days:
    day_num = item["day"]

    col1, col2 = st.columns([0.1, 0.9])

    with col1:
        is_checked = st.checkbox(
            f"Day {day_num}",
            value=st.session_state.completed_days[day_num],
            key=f"day_{day_num}",
            label_visibility="collapsed",
        )
        st.session_state.completed_days[day_num] = is_checked

    with col2:
        # Expandable dropdown for each individual day
        with st.expander(
            f"Day {day_num}: {item['topic']} — *{item['verse']}*"
        ):
            if df is not None and not df.empty:
                b_name = item["search_book"]
                c_num = item["chapter"]

                # Filter CSV for the book and chapter
                verses_to_show = df[
                    (df["Book"].str.contains(b_name, case=False, na=False))
                    & (df["Chapter"] == c_num)
                ]

                if not verses_to_show.empty:
                    for _, row in verses_to_show.iterrows():
                        v_num = row.get("Verse", row.get("verse", ""))
                        v_text = row.get("Text", row.get("text", ""))
                        st.markdown(
                            f"<p><sup>{v_num}</sup> {v_text}</p>",
                            unsafe_allow_html=True,
                        )
                else:
                    st.info(f"Target reference: {item['verse']}")
            else:
                st.info(
                    f"Please verify KJV.csv is uploaded to view full text for {item['verse']}."
                )

# --- RESET BUTTON ---
st.markdown("---")
if st.button("Reset Challenge Progress"):
    for k in st.session_state.completed_days:
        st.session_state.completed_days[k] = False
    st.rerun()
