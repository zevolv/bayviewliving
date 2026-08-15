import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Bayview Living",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Match hero background to the image's own dark navy so there is no visible border.
_LOGO = base64.b64encode(Path("assets/classic_logo_transparent.png").read_bytes()).decode()

_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Raleway:wght@300;400;500&display=swap');

/* ── hide Streamlit chrome ── */
#MainMenu, footer,
[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"],
[data-testid="stSidebar"] { display: none !important; }

/* ── navy page background ── */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] { background-color: #1A2D50 !important; }

/* ── centred content column ── */
[data-testid="stMainBlockContainer"],
section.main > div.block-container {
    max-width: 800px !important;
    padding: 0 2rem 5rem !important;
    margin: 0 auto !important;
}

/* ── page_link as minimal nav text ── */
[data-testid="stPageLink"] {
    display: flex !important;
    justify-content: center !important;
    padding: 0 !important;
}
[data-testid="stPageLink"] a,
[data-testid="stPageLink-NavLink"] {
    display: flex !important;
    justify-content: center !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.65rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.26em !important;
    text-transform: uppercase !important;
    color: rgba(184,146,58,0.7) !important;
    text-decoration: none !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0.15rem 0 !important;
    transition: color 0.2s !important;
}
[data-testid="stPageLink"] a:hover { color: #B8923A !important; }
[data-testid="stPageLink"] p {
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.65rem !important;
    letter-spacing: 0.26em !important;
    text-transform: uppercase !important;
    color: inherit !important;
    margin: 0 !important;
}
[data-testid="stPageLink"] svg { display: none !important; }

/* ── hero: page and logo share the same navy — fully seamless ── */
.bvl-hero {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}
.bvl-hero img { width: 220px; height: auto; display: block; margin: 0 auto; }
.bvl-est {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 0.95rem;
    font-weight: 400;
    letter-spacing: 0.42em;
    color: rgba(201,168,76,0.55);
    text-transform: uppercase;
    margin-top: 0.55rem;
}

/* ── nav ── */
.nav-gap    { height: 0.3rem; }
.nav-rule   { border-top: 1px solid rgba(201,168,76,0.22); margin-bottom: 2.5rem; }

/* ── typography ── */
h1, h2, h3 {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    color: #F0EBE3 !important;
    font-weight: 400 !important;
    letter-spacing: 0.04em;
}
p, li {
    font-family: 'Raleway', sans-serif !important;
    font-weight: 400 !important;
    color: #C8C0B8 !important;
    line-height: 1.8 !important;
}

/* ── page intro ── */
.page-intro { margin-bottom: 2rem; }
.page-intro-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.5rem;
    font-weight: 400;
    color: #F0EBE3;
    letter-spacing: 0.05em;
    margin-bottom: 0.35rem;
}
.page-intro-sub {
    font-family: 'Raleway', sans-serif;
    font-size: 0.86rem;
    font-weight: 400;
    color: #8A8480;
    line-height: 1.7;
    font-style: italic;
}
.gold-rule {
    border: none;
    border-top: 1px solid rgba(201,168,76,0.3);
    margin: 1.4rem 0 1.8rem;
}

/* ── service cards ── */
.svc-card {
    background: #FFFFFF;
    border-top: 2px solid rgba(201,168,76,0.65);
    border-radius: 2px;
    padding: 1.8rem 2rem 1.6rem;
    margin-bottom: 1.4rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.3);
    transition: box-shadow 0.3s;
}
.svc-card:hover { box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
.svc-icon { font-size: 1.1rem; margin-bottom: 0.45rem; opacity: 0.75; }
.svc-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.3rem;
    font-weight: 500;
    color: #0B1622;
    letter-spacing: 0.04em;
    margin-bottom: 0.2rem;
}
.svc-tagline {
    font-family: 'Raleway', sans-serif;
    font-size: 0.67rem;
    font-weight: 400;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(184,146,58,0.75);
    margin-bottom: 0.85rem;
    display: block;
}
.svc-body {
    font-family: 'Raleway', sans-serif;
    font-size: 0.88rem;
    font-weight: 400;
    color: #5A5550;
    line-height: 1.82;
    margin-bottom: 1rem;
}
.svc-items { padding: 0; margin: 0; list-style: none; }
.svc-item {
    padding: 0.45rem 0 0.45rem 1rem;
    border-left: 2px solid rgba(184,146,58,0.22);
    margin-bottom: 0.5rem;
}
.svc-label {
    font-family: 'Raleway', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    color: #1C1912;
}
.svc-desc {
    font-family: 'Raleway', sans-serif;
    font-size: 0.83rem;
    font-weight: 400;
    color: #6A6560;
    line-height: 1.7;
}

/* ── contact ── */
.contact-wrap { text-align: center; padding: 3.5rem 0 2rem; }
.contact-tagline {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.1rem;
    font-style: italic;
    font-weight: 400;
    color: rgba(240,235,227,0.55);
    margin-bottom: 2.8rem;
    display: block;
}
.ig-link {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-family: 'Raleway', sans-serif;
    font-size: 0.72rem;
    font-weight: 400;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(184,146,58,0.72) !important;
    text-decoration: none !important;
    border: 1px solid rgba(201,168,76,0.4);
    padding: 0.8rem 2.2rem;
    transition: all 0.22s;
}
.ig-link:hover {
    color: #B8923A !important;
    border-color: rgba(184,146,58,0.58);
    background: rgba(184,146,58,0.04);
}
.contact-soon {
    font-family: 'Raleway', sans-serif;
    font-size: 0.63rem;
    letter-spacing: 0.28em;
    color: rgba(184,146,58,0.28);
    text-transform: uppercase;
    margin-top: 3.5rem;
}

/* ── responsive ── */
@media (max-width: 480px) {
    .bvl-hero img { width: 170px; }
    .svc-card { padding: 1.3rem 1.1rem 1.1rem; }
    [data-testid="stMainBlockContainer"],
    section.main > div.block-container { padding: 0 1rem 3rem !important; }
}
</style>"""

services_page = st.Page("pages/services.py", title="Services")
contact_page  = st.Page("pages/contact.py",  title="Contact")
pg = st.navigation([services_page, contact_page])

st.markdown(_CSS, unsafe_allow_html=True)
st.markdown(
    f'<div class="bvl-hero"><img src="data:image/png;base64,{_LOGO}" alt="Bayview Living" /><div class="bvl-est">Est. 2026</div></div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="nav-gap"></div>', unsafe_allow_html=True)
_, c1, _, c2, _ = st.columns([2.5, 1, 0.4, 1, 2.5])
with c1:
    st.page_link("pages/services.py", label="Services", use_container_width=True)
with c2:
    st.page_link("pages/contact.py", label="Contact", use_container_width=True)
st.markdown('<div class="nav-rule"></div>', unsafe_allow_html=True)

pg.run()
