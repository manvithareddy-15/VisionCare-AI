import streamlit as st

# Page config
st.set_page_config(
    page_title="VisionCare AI",
    page_icon="👁️",
    layout="centered"
)

# Custom CSS to match the dark UI design
st.markdown("""
<style>

/* =========================================
   VISIONCARE AI - LOGIN PAGE
   NAVY BLUE MONOCHROMATIC THEME
========================================= */

:root {
    --bg: #0b1628;
    --card: #101f35;
    --card-light: #142943;
    --border: #294564;
    --border-light: #3b6085;
    --text: #e5f0ff;
    --text-soft: #a9bfd8;
}


/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background-color: #0b1628 !important;
    color: #e5f0ff !important;
}

header[data-testid="stHeader"] {
    background-color: #0b1628 !important;
}


/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background-color: #0b1628 !important;
}

[data-testid="stSidebar"] > div {
    background-color: #0b1628 !important;
}

[data-testid="stSidebar"] * {
    color: #a9bfd8 !important;
}


/* ACTIVE SIDEBAR PAGE */

[data-testid="stSidebarNav"] [aria-current="page"] {
    background-color: #142943 !important;
    border-radius: 8px !important;
}

[data-testid="stSidebarNav"] [aria-current="page"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
}


/* SIDEBAR NAMES */

[data-testid="stSidebarNav"] a p {
    text-transform: uppercase !important;
}


/* ---------- MAIN CONTAINER ---------- */

.main .block-container {
    background-color: #0b1628 !important;
    max-width: 850px !important;
    padding-top: 2.5rem !important;
}


/* =========================================
   EYE ICON
========================================= */

.login-icon {
    width: 68px;
    height: 68px;

    margin: 25px auto 22px auto;

    background-color: #142943;

    border: 1px solid #294564;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 32px;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.30),
        inset 0 0 12px rgba(111, 159, 201, 0.08);
}


/* =========================================
   WELCOME BACK
========================================= */

.login-title {
    color: #e5f0ff !important;

    font-size: 34px !important;

    font-weight: 700 !important;

    text-align: center !important;

    margin-top: 0 !important;

    margin-bottom: 8px !important;
}


/* =========================================
   SUBTITLE
========================================= */

.login-subtitle {
    color: #a9bfd8 !important;

    font-size: 16px !important;

    text-align: center !important;

    margin-bottom: 32px !important;
}


/* =========================================
   INPUT LABELS
========================================= */

.stTextInput label,
.stSelectbox label {
    color: #a9bfd8 !important;

    font-size: 13px !important;

    font-weight: 600 !important;
}


/* =========================================
   USERNAME + PASSWORD
========================================= */

.stTextInput input {

    background-color: #101f35 !important;

    color: #e5f0ff !important;

    border: 1px solid #3b6085 !important;

    border-radius: 10px !important;

    height: 48px !important;
}


/* INPUT FOCUS */

.stTextInput input:focus {

    border-color: #6f9fc9 !important;

    box-shadow: 0 0 0 1px #6f9fc9 !important;
}


/* PLACEHOLDER */

.stTextInput input::placeholder {

    color: #71869e !important;
}


/* =========================================
   LOGIN AS DROPDOWN
========================================= */

[data-baseweb="select"] > div {

    background-color: #101f35 !important;

    color: #e5f0ff !important;

    border: 1px solid #3b6085 !important;

    border-radius: 10px !important;
}

[data-baseweb="select"] span {
    color: #e5f0ff !important;
}


/* =========================================
   LOGIN BUTTON
========================================= */

.stButton > button {

    background-color: #1b3655 !important;

    color: #ffffff !important;

    border: 1px solid #6f9fc9 !important;

    border-radius: 10px !important;

    min-height: 48px !important;

    padding: 10px 30px !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.25) !important;

    transition: all 0.2s ease !important;
}


/* BUTTON HOVER */

.stButton > button:hover {

    background-color: #294d72 !important;

    border-color: #91b9dc !important;

    color: #ffffff !important;

    transform: translateY(-2px);

    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35) !important;
}


/* BUTTON CLICK */

.stButton > button:active {

    background-color: #142943 !important;

    transform: translateY(0);
}


/* =========================================
   ALERTS
========================================= */

div[data-testid="stAlert"] {

    background-color: #101f35 !important;

    color: #e5f0ff !important;

    border: 1px solid #294564 !important;

    border-radius: 10px !important;
}


/* =========================================
   REMOVE BORDER FROM RANDOM CONTAINERS
========================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background-color: transparent !important;

    border: none !important;
}


/* =========================================
   DIVIDERS
========================================= */

hr {
    border-color: #294564 !important;
}


/* =========================================
   SCROLLBAR
========================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #0b1628;
}

::-webkit-scrollbar-thumb {
    background: #294564;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #3b6085;
}

</style>
""", unsafe_allow_html=True)
# Eye icon + title
st.markdown("""
<div class="login-icon">
    👁️
</div>

<div class="login-title">
    Welcome back
</div>

<div class="login-subtitle">
    Sign in to your VisionCare AI account
</div>
""", unsafe_allow_html=True)

# Login card
st.markdown('<div class="login-card">', unsafe_allow_html=True)

username = st.text_input(
    "USERNAME",
    placeholder="Enter your username"
)

password = st.text_input(
    "PASSWORD",
    placeholder="••••••••",
    type="password"
)

role = st.selectbox(
    "LOGIN AS",
    ["Patient", "Doctor", "Administrator"]
)

login_clicked = st.button("Login")

st.markdown('</div>', unsafe_allow_html=True)
# Handle login
if login_clicked:

    if not username or not password:

        st.error("Please enter both username and password.")

    elif (
        username == "patient1"
        and password == "patient123"
        and role == "Patient"
    ):

        st.session_state["logged_in"] = True
        st.session_state["role"] = "patient"
        st.session_state["username"] = username

        st.success("✅ Patient login successful!")

        st.switch_page("pages/HOME.py")
    elif (
        username == "doctor1"
        and password == "doctor123"
        and role == "Doctor"
    ):

        st.session_state["logged_in"] = True
        st.session_state["role"] = "doctor"
        st.session_state["username"] = username

        st.success("✅ Doctor login successful!")

        st.switch_page("pages/DOCTOR_DASHBOARD.py")

    else:

        st.error("❌ Invalid username, password, or role.")


# Handle login
if login_clicked:

    if not username or not password:
        st.error("Please enter both username and password.")

    # PATIENT
    elif (
        username == "patient1"
        and password == "patient123"
        and role == "Patient"
    ):
        st.session_state.logged_in = True
        st.session_state.role = "patient"
        st.session_state.username = username

        st.success("✅ Patient login successful!")

        st.switch_page("HOME.py")

    # DOCTOR
    elif (
        username == "doctor1"
        and password == "doctor123"
        and role == "Doctor"
    ):
        st.session_state.logged_in = True
        st.session_state.role = "doctor"
        st.session_state.username = username

        st.success("✅ Doctor login successful!")

        # We will create this page later
        st.switch_page("pages/DOCTOR_DASHBOARD.py")

    # ADMIN
    elif (
        username == "admin"
        and password == "admin123"
        and role == "Administrator"
    ):
        st.session_state.logged_in = True
        st.session_state.role = "admin"
        st.session_state.username = username

        st.success("✅ Administrator login successful!")

        # We will create this page later
        st.switch_page("pages/ADMIN_DASHBOARD.py")

    else:
        st.error("❌ Invalid username, password, or role.")
    