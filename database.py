import sqlite3

DATABASE_NAME = "visioncare.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            patient_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            hospital TEXT NOT NULL,
            doctor TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            problem TEXT,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


def save_appointment(
    patient_id,
    patient_name,
    phone,
    hospital,
    doctor,
    appointment_date,
    appointment_time,
    problem
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO appointments (
            patient_id,
            patient_name,
            phone,
            hospital,
            doctor,
            appointment_date,
            appointment_time,
            problem,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'Pending')
    """, (
        patient_id,
        patient_name,
        phone,
        hospital,
        doctor,
        appointment_date,
        appointment_time,
        problem
    ))

    conn.commit()
    conn.close()


def get_all_appointments():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            patient_name,
            phone,
            hospital,
            doctor,
            appointment_date,
            appointment_time,
            problem,
            status
        FROM appointments
        ORDER BY appointment_date, appointment_time
    """)

    appointments = cursor.fetchall()
    conn.close()

    return appointments


def update_appointment_status(appointment_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE appointments
        SET status = ?
        WHERE id = ?
    """, (new_status, appointment_id))

    conn.commit()
    conn.close()


# Create database/table automatically
create_tables()