import streamlit as st

# Tile + popover styles; stPopoverBody toggle is client-side (no server roundtrip).
st.markdown("""<style>
[data-testid="stHorizontalBlock"] [data-testid="stBaseButton-secondary"] {
    height: 190px !important;
    background: #1C2D45 !important;
    border: 1px solid rgba(201,168,76,0.15) !important;
    border-top: 3px solid rgba(201,168,76,0.65) !important;
    border-radius: 0 !important;
    color: #F0EBE3 !important;
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 1.15rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.05em !important;
    line-height: 1.45 !important;
    white-space: pre-line !important;
    text-align: center !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 1.5rem !important;
    box-shadow: 0 4px 18px rgba(0,0,0,0.28) !important;
    transition: all 0.25s ease !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stBaseButton-secondary"]:hover {
    background: #243B58 !important;
    border-top-color: #C9A84C !important;
    box-shadow: 0 8px 28px rgba(0,0,0,0.42) !important;
    transform: translateY(-3px) !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stBaseButton-secondary"]:focus {
    outline: none !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.55), 0 4px 18px rgba(0,0,0,0.28) !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stBaseButton-secondary"] p {
    color: #F0EBE3 !important;
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 1.15rem !important;
    font-weight: 400 !important;
    text-align: center !important;
    line-height: 1.45 !important;
    white-space: pre-line !important;
    margin: 0 !important;
}
/* Popover trigger button (different testid from st.button) */
[data-testid="stHorizontalBlock"] [data-testid="stPopover"] button {
    height: 190px !important;
    width: 100% !important;
    background: #1C2D45 !important;
    border: 1px solid rgba(201,168,76,0.15) !important;
    border-top: 3px solid rgba(201,168,76,0.65) !important;
    border-radius: 0 !important;
    color: #F0EBE3 !important;
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 1.15rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.05em !important;
    line-height: 1.45 !important;
    white-space: pre-line !important;
    text-align: center !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 1.5rem !important;
    box-shadow: 0 4px 18px rgba(0,0,0,0.28) !important;
    transition: all 0.25s ease !important;
    cursor: pointer !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stPopover"] button:hover {
    background: #243B58 !important;
    border-top-color: #C9A84C !important;
    box-shadow: 0 8px 28px rgba(0,0,0,0.42) !important;
    transform: translateY(-3px) !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stPopover"] button:focus {
    outline: none !important;
}
/* Hide the popover chevron arrow */
[data-testid="stHorizontalBlock"] [data-testid="stPopover"] button svg {
    display: none !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stPopover"] button p,
[data-testid="stHorizontalBlock"] [data-testid="stPopover"] button span {
    color: #F0EBE3 !important;
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 1.15rem !important;
    font-weight: 400 !important;
    white-space: pre-line !important;
    line-height: 1.45 !important;
}
[data-testid="stPopoverBody"],
[data-baseweb="popover"],
[data-baseweb="popover"] > div {
    background-color: #FFFFFF !important;
    min-width: 340px !important;
    max-width: 480px !important;
}
[data-testid="stPopoverBody"] p,
[data-testid="stPopoverBody"] li,
[data-baseweb="popover"] p,
[data-baseweb="popover"] li { color: #3A3530 !important; }
</style>""", unsafe_allow_html=True)

st.markdown("""<div class="page-intro">
<div class="page-intro-title">Multidisciplinary Services</div>
<div class="page-intro-sub">Decades of specialised expertise, brought directly to your home, project, or business across Costa Blanca Norte.</div>
</div>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    with st.popover("Home Furnishing\n& Setup", use_container_width=True):
        st.markdown('<span class="svc-tagline">Turnkey setup for your home or property — designed, delivered and built</span>', unsafe_allow_html=True)
        st.markdown("""<div class="svc-body">Setting up a home or vacation rental in Spain involves layers of logistics. We handle the complete process — from layout planning to final assembly — so your space is ready to live in without the hassle.</div>
<ul class="svc-items">
<li class="svc-item"><div class="svc-label">Design &amp; Sourcing</div><div class="svc-desc">Spatial layout guidance, practical furnishing choices, and procurement within your budget.</div></li>
<li class="svc-item"><div class="svc-label">Logistics &amp; Assembly</div><div class="svc-desc">Local pickup, transport, and assembly — local suppliers and custom pieces.</div></li>
<li class="svc-item"><div class="svc-label">Move-In Ready Setup</div><div class="svc-desc">Final fitting, minor fixes, and full preparation for personal use or rental listings.</div></li>
</ul>""", unsafe_allow_html=True)

with col2:
    with st.popover("VIP Airport\n& Arrival", use_container_width=True):
        st.markdown('<span class="svc-tagline">Private, eco-friendly transport between La Marina Baixa &amp; Alicante Airport</span>', unsafe_allow_html=True)
        st.markdown("""<div class="svc-body">Punctual, comfortable, and direct connections for residents and guests travelling across Costa Blanca Norte.</div>
<ul class="svc-items">
<li class="svc-item"><div class="svc-label">Airport Routes</div><div class="svc-desc">Direct, stress-free transfers to and from Alicante Airport (ALC).</div></li>
<li class="svc-item"><div class="svc-label">Grocery &amp; Meal Add-On</div><div class="svc-desc">Pre-book a grocery order or meal delivery alongside your transfer — basic essentials, simple &amp; healthy, or hearty meals — delivered to your door on arrival.</div></li>
</ul>""", unsafe_allow_html=True)

with col3:
    with st.popover("Data Analytics\n& Web", use_container_width=True):
        st.markdown('<span class="svc-tagline">From complex spreadsheets to fully deployed web applications</span>', unsafe_allow_html=True)
        st.markdown("""<div class="svc-body">Two decades of experience in data architecture and knowledge engineering. We transform raw information into clean, structured tools and custom web applications.</div>
<ul class="svc-items">
<li class="svc-item"><div class="svc-label">Data Management &amp; Automation</div><div class="svc-desc">Spreadsheet cleanup, custom data modelling, automated workflows, and complex reporting systems.</div></li>
<li class="svc-item"><div class="svc-label">Custom Web Development</div><div class="svc-desc">Fast, clean, data-driven web applications built with modern frameworks.</div></li>
<li class="svc-item"><div class="svc-label">Business Intelligence</div><div class="svc-desc">Interactive dashboards, system integrations, and structured catalogues designed for clarity and usability.</div></li>
</ul>""", unsafe_allow_html=True)

