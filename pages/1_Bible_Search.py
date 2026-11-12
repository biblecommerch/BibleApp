# Import pandas for reading spreadsheets and streamlit for building the app
import pandas as pd
import streamlit as st

# Set the page title for your search tool
st.set_page_config(
    page_title="Bible Verse Search", page_icon="📖", layout="wide"
)

# Main Title for the search page
st.title("📖 Bible Verse Search Tool")
st.write(
    "Search through your CSV database instantly by keyword, book, or topic!"
)


# Load the data using cache to keep things fast
@st.cache_data
def load_data():
  return pd.read_csv("KJV.csv")


# Run the load function
df = load_data()

# Create the search box input
search_query = st.text_input(
    "Enter a keyword or topic (e.g., *love*, *faith*, *peace*):"
)

# Filter and display results if the user types something
if search_query:
  results = df[
      df.select_dtypes(include=["object"])
      .apply(lambda col: col.str.contains(search_query, case=False, na=False))
      .any(axis=1)
  ]

  st.write(f"Found **{len(results)}** results for *'{search_query}'*:")
  st.dataframe(results)

else:
  st.info("Type a word above to search your Bible database.")
