import re

# ==========================================
# CENTRALIZED SITE BRANDING & ANCHOR CONFIG
# ==========================================
# Update APP_NAME and taglines in this one place to reflect across pages
# that import from site_config.py.
APP_NAME = "Mel's Bible Apps"
APP_TAGLINE = "Read, Research, &amp; Stay Centered on God's Word"
APP_FOOTER_TAGLINE = "Read, Research &amp; Grow in Scripture"


def name_to_anchor(text: str) -> str:
    """Converts heading text into a clean HTML anchor ID (e.g., 'Mel's Bible Apps' -> '#mel-s-bible-apps')."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return f"#{slug}"
