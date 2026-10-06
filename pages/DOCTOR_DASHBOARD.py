import streamlit as st
from database import get_all_appointments,update_appointment_status

st.set_page_config(
    page_title="Doctor Dashboard",
    page_icon="👨‍⚕️",
    layout="wide"
)

# -----------------------------
# LOGIN CHECK
# -----------------------------


# -----------------------------
# DOCTOR CHECK
# -----------------------------

if st.session_state.get("role") != "doctor":
    st.error("You do not have permission to access this page.")
    st.stop()

# -----------------------------
# DASHBOARD
# -----------------------------

st.title("👨‍⚕️ Doctor Dashboard")

doctor_name = st.session_state.get(
    "username",
    "Doctor"
)

st.write(f"Welcome, Dr. {doctor_name} 👋")

st.divider()

st.subheader("📅 Appointments")

appointments = get_all_appointments()

if appointments:

    for appointment in appointments:

        (
            appointment_id,
            patient_name,
            phone,
            hospital,
            doctor,
            appointment_date,
            appointment_time,
            problem,
            status
        ) = appointment

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:
                st.write(f"### 👤 {patient_name}")

                st.write(f"📞 **Phone:** {phone}")
                st.write(f"🏥 **Hospital:** {hospital}")
                st.write(f"👨‍⚕️ **Doctor:** {doctor}")
                st.write(f"📅 **Date:** {appointment_date}")
                st.write(f"⏰ **Time:** {appointment_time}")
                st.write(f"🩺 **Problem:** {problem}")

                if status == "Pending":
                    st.warning("🟡 Pending")
                else:
                    st.success("🟢 Completed")

            with col2:

                if status == "Pending":

                    if st.button(
                        "✅ Mark as Completed",
                        key=f"complete_{appointment_id}"
                    ):

                        update_appointment_status(
                            appointment_id,
                            "Completed"
                        )

                        st.success("Appointment marked as completed.")

                        st.rerun()

                else:

                    st.button(
                        "✅ Completed",
                        key=f"completed_{appointment_id}",
                        disabled=True
                    )

else:

    st.info("No appointments have been booked yet.")


# Statistics
st.divider()

total = len(appointments)

pending = sum(
    1 for appointment in appointments
    if appointment[8] == "Pending"
)

completed = sum(
    1 for appointment in appointments
    if appointment[8] == "Completed"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Appointments", total)

with col2:
    st.metric("Pending", pending)

with col3:
    st.metric("Completed", completed)