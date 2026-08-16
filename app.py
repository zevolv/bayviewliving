import streamlit as st
import base64
from pathlib import Path

from PIL import Image as _Image

st.set_page_config(
    page_title="Bayview Living",
    page_icon=_Image.open("assets/favicon.png"),
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Match hero background to the image's own dark navy so there is no visible border.
_LOGO = base64.b64encode(Path("assets/bvl_transparent.png").read_bytes()).decode()

_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Raleway:wght@300;400;500&display=swap');

/* ── hide Streamlit chrome ── */
#MainMenu, footer,
[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"],
[data-testid="stSidebar"] { display: none !important; }

/* ── white page background ── */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] { background-color: #FFFFFF !important; }

/* ── centred content column ── */
[data-testid="stMainBlockContainer"],
section.main > div.block-container {
    max-width: 800px !important;
    padding: 0 2rem 5rem !important;
    margin: 0 auto !important;
}

/* ── unified dark header block ── */
.bvl-header {
    background: #1C2D45;
    margin: 0 -2rem;
    padding: 2rem 2.5rem;
    display: flex;
    align-items: center;
    gap: 2rem;
}
.bvl-header img {
    width: 90px;
    height: auto;
    flex-shrink: 0;
    transform: translateY(-0.6rem);
}
.bvl-brand {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transform: translateY(0.6rem);
}
.bvl-name {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 2.4rem;
    font-weight: 500;
    color: #E8D5A3;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    line-height: 1;
}
.bvl-est {
    font-family: 'Raleway', sans-serif;
    font-size: 0.72rem;
    font-weight: 400;
    letter-spacing: 0.38em;
    color: rgba(232,213,163,0.55);
    text-transform: uppercase;
    margin-top: 0.5rem;
}
/* nav: white background, dark gold text */
[data-testid="stMainBlockContainer"] [data-testid="stHorizontalBlock"]:has([data-testid="stPageLink"]) {
    background-color: #FFFFFF !important;
    margin-left: -2rem !important;
    margin-right: -2rem !important;
    padding: 0.8rem 2rem !important;
    border-bottom: 1px solid rgba(11,22,34,0.18) !important;
}
[data-testid="stPageLink"] {
    display: flex !important;
    justify-content: center !important;
    padding: 0 !important;
}
[data-testid="stPageLink"] a,
[data-testid="stPageLink-NavLink"] {
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    color: #1C2D45 !important;
    text-decoration: none !important;
    background: transparent !important;
    border: none !important;
    padding: 0.3rem 0 !important;
    transition: color 0.2s !important;
}
[data-testid="stPageLink"] a:hover { color: #0B1622 !important; }
[data-testid="stPageLink"] p {
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    color: #1C2D45 !important;
    margin: 0 !important;
}
[data-testid="stPageLink"] svg { display: none !important; }
/* separator between nav and content */
.nav-rule {
    display: none;
}

/* ── typography (light background) ── */
h1, h2, h3 {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    color: #0B1622 !important;
    font-weight: 400 !important;
    letter-spacing: 0.04em;
}
p, li {
    font-family: 'Raleway', sans-serif !important;
    font-weight: 400 !important;
    color: #3A3530 !important;
    line-height: 1.8 !important;
}

/* ── page intro (white section below dark nav band) ── */
.page-intro {
    background: #FFFFFF;
    margin: 0 -2rem;
    padding: 1.8rem 2rem 2rem;
    text-align: left;
    border-top: none;
}
.page-intro-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.5rem;
    font-weight: 400;
    color: #0B1622;
    letter-spacing: 0.05em;
    margin-bottom: 0.35rem;
}
.page-intro-sub {
    font-family: 'Raleway', sans-serif;
    font-size: 0.86rem;
    font-weight: 400;
    color: #3A3530;
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
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #8B6520;
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
    font-weight: 700;
    color: #0B1622;
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
    color: #3A3530;
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
    color: rgba(154,114,40,0.9) !important;
    text-decoration: none !important;
    border: 1px solid rgba(154,114,40,0.5);
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
    color: #5A5550;
    text-transform: uppercase;
    margin-top: 3.5rem;
}

/* ── responsive ── */
@media (max-width: 480px) {
    .bvl-header img { width: 170px; }
    .svc-card { padding: 1.3rem 1.1rem 1.1rem; }
    [data-testid="stMainBlockContainer"],
    section.main > div.block-container { padding: 0 1rem 3rem !important; }
}
</style>"""

services_page = st.Page("pages/services.py", title="Services", url_path="services")
contact_page  = st.Page("pages/contact.py",  title="Contact",  url_path="contact")
pg = st.navigation([services_page, contact_page])

st.markdown(_CSS, unsafe_allow_html=True)

st.markdown(
    f'<div class="bvl-header"><img src="data:image/png;base64,{_LOGO}" alt="Bayview Living" /><div class="bvl-brand"><div class="bvl-name">Bayview Living</div><div class="bvl-est">Est.&nbsp; 2026</div></div></div>',
    unsafe_allow_html=True,
)
_, c1, _, c2, _ = st.columns([1.8, 1.8, 0.4, 1.8, 1.8])
with c1:
    st.page_link(services_page, label="Services", use_container_width=True)
with c2:
    st.page_link(contact_page, label="Contact", use_container_width=True)
# Services page shows intro text inside dark band; Contact page closes with nav-rule
if pg.title == "Services":
    st.markdown("""<div class="page-intro"><div class="page-intro-title">Multidisciplinary Services</div><div class="page-intro-sub">Decades of specialised expertise, brought directly to your home, project, or business across Costa Blanca Norte.</div></div>""", unsafe_allow_html=True)
else:
    st.markdown('<div class="nav-rule"></div>', unsafe_allow_html=True)

pg.run()
