import streamlit as st
from datetime import date
from database import create_tables, save_appointment

create_tables()

# =========================================
# MONOCHROMATIC NAVY THEME
# =========================================

st.markdown("""
<style>

/* ==============================
   WHITE / LIGHT THEME
============================== */

.stApp {
    background-color: #ffffff !important;
    color: #252a36 !important;
}

/* Header */
header[data-testid="stHeader"] {
    background-color: #ffffff !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}

[data-testid="stSidebar"] > div {
    background-color: #ffffff !important;
}

[data-testid="stSidebar"] * {
    color: #252a36 !important;
}

/* Main content */
.main .block-container {
    background-color: #ffffff !important;
    color: #252a36 !important;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #252a36 !important;
}

/* Normal text */
p, label {
    color: #394150 !important;
}

/* Text inputs */
.stTextInput input,
.stTextArea textarea {
    background-color: #f5f7fa !important;
    color: #252a36 !important;
    border: 1px solid #d9dee7 !important;
    border-radius: 9px !important;
}

/* Date input */
[data-testid="stDateInput"] input {
    background-color: #f5f7fa !important;
    color: #252a36 !important;
    border: 1px solid #d9dee7 !important;
}

/* Select boxes */
[data-baseweb="select"] > div {
    background-color: #f5f7fa !important;
    color: #252a36 !important;
    border-color: #d9dee7 !important;
}

[data-baseweb="select"] span {
    color: #252a36 !important;
}

/* Buttons */
.stButton > button {
    background-color: #f5f7fa !important;
    color: #252a36 !important;
    border: 1px solid #cbd2dc !important;
    border-radius: 10px !important;
    min-height: 45px !important;
    padding: 8px 22px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;
    transition: all 0.2s ease !important;
}

/* Button hover */
.stButton > button:hover {
    background-color: #e9edf3 !important;
    color: #1d2430 !important;
    border-color: #aeb8c6 !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.12) !important;
}

/* Button click */
.stButton > button:active {
    background-color: #dde3eb !important;
    transform: translateY(0px);
}

/* Disabled buttons */
.stButton > button:disabled {
    background-color: #f1f3f6 !important;
    color: #a0a7b2 !important;
    border-color: #e1e4e9 !important;
}

/* Cards / containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff !important;
    border: 1px solid #e1e5eb !important;
    border-radius: 14px !important;
}

/* Alert boxes */
div[data-testid="stAlert"] {
    background-color: #f5f7fa !important;
    color: #252a36 !important;
    border: 1px solid #d9dee7 !important;
    border-radius: 12px !important;
}

/* Dividers */
hr {
    border-color: #e1e5eb !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: #ffffff !important;
}

[data-testid="stFileUploader"] section {
    background-color: #f5f7fa !important;
}

/* Camera */
[data-testid="stCameraInput"] {
    background-color: #ffffff !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #ffffff;
}

::-webkit-scrollbar-thumb {
    background: #d1d7df;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #aeb7c3;
}

</style>
""", unsafe_allow_html=True)

from database import create_tables, save_appointment
create_tables()
if not st.session_state.get("logged_in", False):
    st.error("Please login first.")
    st.stop()


    # Check login
if not st.session_state.get("logged_in", False):
    st.error("Please login first.")
    st.stop()

# Check patient role
if st.session_state.get("role") != "patient":
    st.error("You do not have permission to access this page.")
    st.stop()
    
st.set_page_config(page_title="Doctor Appointment",
                   page_icon="👨‍⚕️", layout="centered")

st.title("👨‍⚕️ Vision Eye Care - Doctor Appointment Booking")
st.markdown("Book an appointment with an eye specialist in Hyderabad.")

# -------------------------------
# HYDERABAD DATA (2 DOCTORS EACH)
# -------------------------------
hyderabad_data = {
    "Apollo Eye Hospital": [
        "Dr. Priya Sharma - Eye Specialist",
        "Dr. Rahul Verma - Retina Specialist"
    ],
    "LV Prasad Eye Institute": [
        "Dr. Kavya Reddy - Cornea Specialist",
        "Dr. Ramesh Kumar - Pediatric Eye Specialist"
    ],
    "Care Hospital": [
        "Dr. Nisha Patel - General Ophthalmologist",
        "Dr. Arjun Reddy - Cataract Specialist"
    ],
    "Maxivision Eye Hospital": [
        "Dr. Anil Kumar - Cataract Specialist",
        "Dr. Sneha Gupta - LASIK Specialist"
    ],
    "Centre for Sight": [
        "Dr. Meena Gupta - LASIK Specialist",
        "Dr. Rohit Sharma - Retina Specialist"
    ],
    "Dr. Agarwal’s Eye Hospital": [
        "Dr. Suresh Babu - Retina Specialist",
        "Dr. Kavitha Rao - Eye Surgeon"
    ],
    "Medivision Eye & Health Care": [
        "Dr. Swathi Reddy - Eye Specialist",
        "Dr. Mahesh Babu - General Ophthalmologist"
    ],
    "Win Vision Eye Hospitals": [
        "Dr. Kiran Kumar - Glaucoma Specialist",
        "Dr. Divya Nair - Cornea Specialist"
    ],
    "Eye Care Hospital (Secunderabad)": [
        "Dr. Rajesh - Ophthalmologist",
        "Dr. Pooja Sharma - Pediatric Eye Specialist"
    ],
    "Sankara Eye Hospital": [
        "Dr. Harish - Cataract Specialist",
        "Dr. Lakshmi Devi - Retina Specialist"
    ],
    "Ojas Eye Hospital": [
        "Dr. Deepa - Pediatric Eye Specialist",
        "Dr. Naveen Kumar - Eye Surgeon"
    ],
    "Shreya Eye Care Centre": [
        "Dr. Mahesh - General Ophthalmologist",
        "Dr. Anusha Reddy - LASIK Specialist"
    ]
}

# -------------------------------
# CITY FIXED
# -------------------------------
st.subheader("📍 City: Hyderabad")

# -------------------------------
# HOSPITAL SELECTION
# -------------------------------
hospital = st.selectbox("Select Hospital", list(hyderabad_data.keys()))

# -------------------------------
# DOCTOR SELECTION
# -------------------------------
doctor = st.selectbox("Select Doctor", hyderabad_data[hospital])

# -------------------------------
# TIME SLOTS
# -------------------------------
time_slots = ["9:00 AM", "10:30 AM", "12:00 PM", "2:00 PM", "4:00 PM"]

appointment_date = st.date_input(
    "Choose Appointment Date",
    min_value=date.today()
)

appointment_time = st.selectbox("Choose Time Slot", time_slots)

# -------------------------------
# PATIENT DETAILS
# -------------------------------
patient_name = st.text_input("Patient Name")
phone = st.text_input("Phone Number")
problem = st.text_area("Describe Your Eye Problem")

# -------------------------------
# BOOKING
# -------------------------------
if st.button("Book Appointment"):

    if patient_name.strip() == "":
        st.error("Please enter patient name.")

    elif phone.strip() == "":
        st.error("Please enter phone number.")

    else:

        patient_id = st.session_state.get("user_id", 1)

        save_appointment(
            patient_id=None,
            patient_name=patient_name,
            phone=phone,
            hospital=hospital,
            doctor=doctor,
            appointment_date=str(appointment_date),
            appointment_time=appointment_time,
            problem=problem
        )

        st.success("✅ Appointment booked successfully!")
        st.info(
            f"""
            **Hospital:** {hospital}

            **Doctor:** {doctor}

            **Date:** {appointment_date}

            **Time:** {appointment_time}

            **Status:** Pending
            """
        )
