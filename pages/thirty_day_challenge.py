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
        <li><b>Days 1 to 7: Foundations of Faith and Trust</b> establishing where we came from and anchoring our trust in God as our protector and shepherd.</li>
        <li><b>Days 8 to 14: The Heart and Life of Christ</b> following the prophecy, love, and teachings of Jesus to understand His heart.</li>
        <li><b>Days 15 to 21: Grace, Forgiveness, and New Life</b> exploring what it means to be a new creation through grace, walking in the Spirit, and loving one another.</li>
        <li><b>Days 22 to 30: Strength, Peace, and Eternal Hope</b> equipping ourselves with His strength, standing strong in trials, and living with joyful anticipation.</li>
    </ul>
    <p style="margin-bottom:0; font-size: 0.9em; color: #b7d5b8;">Click on any day below to open the dropdown and read the daily anchor verse and reflection.</p>
</div>
""",
    unsafe_allow_html=True,
)

# --- 30 DAY CHALLENGE DATA (Single Verse + Commentary) ---
challenge_days = [
    {
        "day": 1,
        "verse": "Genesis 1:1",
        "search_book": "Genesis",
        "chapter": 1,
        "commentary": "Everything starts with God. Before the chaos of life or your daily worries, His creative hand was already establishing order and purpose for you.",
    },
    {
        "day": 2,
        "verse": "Psalm 23:1",
        "search_book": "Psalms",
        "chapter": 23,
        "commentary": "You are never walking alone or forgotten. When you trust God as your shepherd, He actively provides for your needs and brings peace to your mind.",
    },
    {
        "day": 3,
        "verse": "Proverbs 3:5",
        "search_book": "Proverbs",
        "chapter": 3,
        "commentary": "True peace comes from releasing the need to figure everything out on your own and leaning fully into God's infinite wisdom.",
    },
    {
        "day": 4,
        "verse": "Psalm 46:1",
        "search_book": "Psalms",
        "chapter": 46,
        "commentary": "God is your ever-present refuge. When storms arise around you, you can run to His unchanging strength and find absolute safety.",
    },
    {
        "day": 5,
        "verse": "Proverbs 18:10",
        "search_book": "Proverbs",
        "chapter": 18,
        "commentary": "The name of the Lord is a strong tower. Whenever fear or anxiety tries to creep in, call upon His name to find immediate shelter.",
    },
    {
        "day": 6,
        "verse": "Psalm 119:105",
        "search_book": "Psalms",
        "chapter": 119,
        "commentary": "His Word is a reliable lamp to guide your daily steps, illuminating the path right in front of you so you never have to guess your way.",
    },
    {
        "day": 7,
        "verse": "Isaiah 41:10",
        "search_book": "Isaiah",
        "chapter": 41,
        "commentary": "God commands you not to fear because He is personally with you, upholding you with His righteous right hand through every season.",
    },
    {
        "day": 8,
        "verse": "Isaiah 9:6",
        "search_book": "Isaiah",
        "chapter": 9,
        "commentary": "Jesus came as our Wonderful Counselor and Prince of Peace, bringing everlasting comfort and stability to a restless world.",
    },
    {
        "day": 9,
        "verse": "John 3:16",
        "search_book": "John",
        "chapter": 3,
        "commentary": "This is the ultimate anchor of the Christian faith. God loved you so deeply that He gave His Son so you could have everlasting life.",
    },
    {
        "day": 10,
        "verse": "Matthew 6:33",
        "search_book": "Matthew",
        "chapter": 6,
        "commentary": "When you put God's kingdom and righteousness first, He promises to faithfully take care of all your daily needs.",
    },
    {
        "day": 11,
        "verse": "John 8:12",
        "search_book": "John",
        "chapter": 8,
        "commentary": "Jesus is the light of the world. Anyone who follows Him will never walk in darkness, but will have the light of life.",
    },
    {
        "day": 12,
        "verse": "John 10:11",
        "search_book": "John",
        "chapter": 10,
        "commentary": "The Good Shepherd willingly lays down His life for His sheep, proving the immense depth of His personal devotion to you.",
    },
    {
        "day": 13,
        "verse": "John 14:27",
        "search_book": "John",
        "chapter": 14,
        "commentary": "Jesus gives a supernatural peace that the world cannot give, telling your heart not to be troubled or afraid.",
    },
    {
        "day": 14,
        "verse": "John 15:5",
        "search_book": "John",
        "chapter": 15,
        "commentary": "Staying connected to Christ is the secret to bearing fruit. Apart from Him, we cannot accomplish lasting spiritual work.",
    },
    {
        "day": 15,
        "verse": "2 Corinthians 5:17",
        "search_book": "2 Corinthians",
        "chapter": 5,
        "commentary": "In Christ, you are a brand new creation. Your past mistakes do not define you because the old has gone and the new has come.",
    },
    {
        "day": 16,
        "verse": "Ephesians 2:8",
        "search_book": "Ephesians",
        "chapter": 2,
        "commentary": "Salvation is a precious gift from God by grace through faith, meaning you don't have to earn His love through perfection.",
    },
    {
        "day": 17,
        "verse": "Romans 8:1",
        "search_book": "Romans",
        "chapter": 8,
        "commentary": "There is now zero condemnation for those who belong to Christ Jesus. You can walk free from guilt and shame.",
    },
    {
        "day": 18,
        "verse": "Galatians 5:22",
        "search_book": "Galatians",
        "chapter": 5,
        "commentary": "Allow the Holy Spirit to cultivate beautiful fruit in your character, starting with love, joy, and peace.",
    },
    {
        "day": 19,
        "verse": "1 Corinthians 13:4",
        "search_book": "1 Corinthians",
        "chapter": 13,
        "commentary": "Love is patient and kind. Choosing to love others the way Christ loves us transforms our everyday interactions.",
    },
    {
        "day": 20,
        "verse": "James 4:8",
        "search_book": "James",
        "chapter": 4,
        "commentary": "God invites you to draw near to Him. As you take a step toward Him in prayer, He promises to draw close to you.",
    },
    {
        "day": 21,
        "verse": "1 John 1:9",
        "search_book": "1 John",
        "chapter": 1,
        "commentary": "God is completely faithful and just to forgive our sins and cleanse us from all unrighteousness whenever we come to Him honestly.",
    },
    {
        "day": 22,
        "verse": "Ephesians 6:10",
        "search_book": "Ephesians",
        "chapter": 6,
        "commentary": "Be strong in the Lord and in His mighty power rather than relying on your own limited human strength.",
    },
    {
        "day": 23,
        "verse": "Philippians 4:6",
        "search_book": "Philippians",
        "chapter": 4,
        "commentary": "Do not be anxious about anything. Instead, bring every single worry to God through prayer wrapped in a thankful heart.",
    },
    {
        "day": 24,
        "verse": "Philippians 4:13",
        "search_book": "Philippians",
        "chapter": 4,
        "commentary": "You can face any challenge or obstacle that comes your way because Christ gives you the inner strength you need.",
    },
    {
        "day": 25,
        "verse": "Hebrews 4:12",
        "search_book": "Hebrews",
        "chapter": 4,
        "commentary": "God's Word is alive and active, able to pierce through confusion and speak directly to the deepest thoughts of your heart.",
    },
    {
        "day": 26,
        "verse": "Hebrews 11:1",
        "search_book": "Hebrews",
        "chapter": 11,
        "commentary": "Faith is the confident assurance in things we hope for and the deep conviction of things we cannot yet see.",
    },
    {
        "day": 27,
        "verse": "1 Peter 2:9",
        "search_book": "1 Peter",
        "chapter": 2,
        "commentary": "You are chosen, royal, and a treasured child of God, called out of darkness into His marvelous light.",
    },
    {
        "day": 28,
        "verse": "Romans
