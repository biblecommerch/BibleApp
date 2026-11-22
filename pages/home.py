import streamlit as st
from supabase import create_client


@st.cache_resource
def get_supabase():
    """Creates and caches the Supabase client using Streamlit secrets."""
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)


def require_email_to_save():
    """Returns the active user's email if signed in, or None if missing."""
    email = st.session_state.get("user_email", "").strip().lower()
    return email if email else None


def _is_valid_email(email):
    return bool(email and "@" in email and "." in email.split("@")[-1])


def render_sidebar_auth():
    """Renders the sidebar account/sync box and privacy link across pages."""
    with st.sidebar:
        st.markdown("### 📖 Save Your Progress")
        st.write(
            "Enter your email to save your challenge streak and favorite verses, "
            "plus get notified when new features launch."
        )

        default_email = st.session_state.get("user_email", "")
        user_email = st.text_input(
            "Email address",
            value=default_email,
            placeholder="you@example.com",
            key="sidebar_email",
        )

        if st.button("Save & Stay Updated", use_container_width=True, key="sidebar_submit"):
            cleaned_email = user_email.strip().lower()
            if _is_valid_email(cleaned_email):
                try:
                    db = get_supabase()
                    db.table("users").upsert({
                        "email": cleaned_email,
                        "site_updates": True,
                    }).execute()
                    st.session_state["user_email"] = cleaned_email
                    st.success("🎉 Saved successfully!")
                except Exception:
                    st.error("Could not save. Please try again.")
            else:
                st.warning("Please enter a valid email address.")

        st.markdown("---")
        st.page_link("pages/privacy.py", label="🔒 Privacy Policy")
