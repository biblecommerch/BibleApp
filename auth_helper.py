import streamlit as st
from supabase import create_client, Client

# Initialize and cache the Supabase client connection using Streamlit secrets
@st.cache_resource
def get_supabase() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

def render_sidebar_auth():
    """
    Renders the state-of-the-art sidebar account & site updates manager.
    - Manages the user's email ID in Streamlit session state across all pages.
    - Handles account active state, sign-out, and newsletter/site update opt-ins.
    """
    supabase = get_supabase()
    st.sidebar.markdown("---")
    st.sidebar.subheader("👤 Account & Sync")

    # Check if a user email is already stored in the current session
    current_email = st.session_state.get("user_email", "")

    if current_email:
        # User is recognized; show their email and a sign-out option
        st.sidebar.success(f"Signed in as:\n**{current_email}**")
        if st.sidebar.button("Switch / Sign Out", key="sidebar_signout"):
            st.session_state["user_email"] = ""
            st.success("Signed out for this session.")
            st.rerun()
    else:
        # User is a guest; invite them to enter their email for cross-device syncing
        st.sidebar.caption("Enter your email to sync saved verses, study cards, and challenge progress across devices.")
        
        with st.sidebar.form("sidebar_email_form"):
            email_input = st.text_input("Email address", placeholder="you@example.com")
            subscribe_updates = st.checkbox("☑️ Notify me when new Bible Focus features launch", value=True)
            submit_btn = st.form_submit_button("Save & Sync Account")

            if submit_btn:
                if email_input and "@" in email_input and "." in email_input:
                    st.session_state["user_email"] = email_input
                    try:
                        # Upsert email and update preferences in the Supabase 'users' table
                        supabase.table("users").upsert({
                            "email": email_input,
                            "site_updates": subscribe_updates
                        }).execute()
                        st.sidebar.success("✨ Account active!")
                        st.rerun()
                    except Exception as e:
                        st.sidebar.error("Could not sync with database. Check secrets.")
                else:
                    st.sidebar.warning("Please enter a valid email address.")

def require_email_to_save(item_type: str, item_value: str, button_label="💾 Save to My Account"):
    """
    Plug-and-play inline save helper.
    - If user email is known: Renders a 1-click button that writes directly to Supabase.
    - If user email is NOT known: Renders a smooth inline prompt asking for their email 
      to unlock saving instantly without a password.
    """
    supabase = get_supabase()
    current_email = st.session_state.get("user_email", "")

    if current_email:
        # Recognized user: 1-click save button
        if st.button(button_label, key=f"save_act_{item_type}_{item_value}"):
            try:
                supabase.table("user_progress").insert({
                    "email": current_email,
                    "item_type": item_type,
                    "item_value": item_value
                }).execute()
                st.success("✨ Saved successfully to your account!")
            except Exception as e:
                st.error(f"Save error: {e}")
    else:
        # Unrecognized visitor: Prompt for email inline
        st.info("🔒 **Enter your email to save** your progress & study cards across devices:")
        inline_email = st.text_input("Your email address", key=f"inline_email_{item_type}_{item_value}", placeholder="you@example.com")
        if st.button("Unlock & Save", key=f"inline_unlock_{item_type}_{item_value}"):
            if inline_email and "@" in inline_email:
                st.session_state["user_email"] = inline_email
                try:
                    # Automatically register the user and save their item in one action
                    supabase.table("users").upsert({"email": inline_email, "site_updates": True}).execute()
                    supabase.table("user_progress").insert({
                        "email": inline_email,
                        "item_type": item_type,
                        "item_value": item_value
                    }).execute()
                    st.success("🎉 Account linked and item saved!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter a valid email address.")
