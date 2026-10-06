

import streamlit as st

# Check whether user is logged in
if not st.session_state.get("logged_in", False):
    st.switch_page("pages/login.py")
if st.session_state.get("role") != "patient":
    st.error("You do not have permission to access this page.")
    st.stop()
# PAGE CONFIG
st.set_page_config(page_title="Home", page_icon="👁️", layout="centered")

# UI
st.markdown("""
<style>

/* ==============================
   MONOCHROMATIC HOME PAGE
   ============================== */

:root {
    --bg: #0b1628;
    --surface: #0f1f35;
    --surface2: #142943;
    --border: #294564;
    --border-light: #3b6085;
    --text: #e5f0ff;
    --text-soft: #a9bfd8;
}


/* MAIN APP */
.stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
}


/* HEADER */
header[data-testid="stHeader"] {
    background: var(--bg) !important;
}


/* SIDEBAR */
[data-testid="stSidebar"] {
    background: var(--bg) !important;
}

[data-testid="stSidebar"] > div {
    background: var(--bg) !important;
}

[data-testid="stSidebar"] * {
    color: var(--text) !important;
}


/* MAIN CONTENT */
.main .block-container {
    background: var(--bg) !important;
    padding-top: 2rem;
}


/* REMOVE OLD GRADIENT / BACKGROUND */
.main {
    background: var(--bg) !important;
}


/* HOME HERO */
.home-container {
    background: var(--bg) !important;
    padding: 40px;
    border-radius: 20px;
    min-height: 650px;
}


/* TITLE */
.home-title {
    color: var(--text) !important;
    text-align: center;
    font-size: 42px;
    font-weight: 700;
}


/* SUBTITLE */
.home-subtitle {
    color: var(--text-soft) !important;
    text-align: center;
    font-size: 22px;
    margin-bottom: 35px;
}


/* SERVICE CARDS */
.service-card {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px;
    padding: 28px;
    min-height: 200px;
}


/* CARD TITLES */
.service-card h2 {
    color: var(--text) !important;
}


/* CARD TEXT */
.service-card p {
    color: var(--text-soft) !important;
}


/* ALL BUTTONS */
.stButton > button {

    background: var(--surface2) !important;

    color: var(--text) !important;

    border: 1px solid var(--border-light) !important;

    border-radius: 12px !important;

    min-height: 48px !important;

    padding: 10px 25px !important;

    font-size: 16px !important;

    font-weight: 600 !important;

    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;

    transition: all 0.2s ease !important;
}


/* BUTTON HOVER */
.stButton > button:hover {

    background: #1b3655 !important;

    color: #ffffff !important;

    border-color: #6f9fc9 !important;

    transform: translateY(-2px);

    box-shadow: 0 7px 18px rgba(0,0,0,0.35) !important;
}


/* BUTTON CLICK */
.stButton > button:active {

    background: #244563 !important;

    transform: translateY(0px);

}


/* DIVIDERS */
hr {
    border-color: var(--border) !important;
}


/* TEXT */
h1, h2, h3, h4, h5, h6 {
    color: var(--text) !important;
}

p {
    color: var(--text-soft) !important;
}


/* REMOVE WHITE BLOCKS */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
}


/* SCROLLBAR */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg);
}

::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--border-light);
}

</style>
""", unsafe_allow_html=True)

st.title(" VisionCare AI Dashboard")
st.markdown("### Choose a service 👇")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👁️ Eye Analysis")
    if st.button("Analyse my eye"):
        st.switch_page("pages/EYE_ANALYSIS.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👨‍⚕️ Doctor Appointment")
    if st.button("Book Appointment"):
        st.switch_page("pages/DOCTOR_APPOINTMENT.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Logout
st.markdown("---")

if st.button("🚪 Logout"):

    st.session_state.clear()

    st.switch_page("login.py")