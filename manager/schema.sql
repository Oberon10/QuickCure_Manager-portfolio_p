DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS appointments;


CREATE TABLE patient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone_number TEXT UNIQUE NOT NULL,
    gender TEXT NOT NULL,
    age INTEGER NOT NULL,
    blood_group TEXT NOT NULL
);

CREATE TABLE doctor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    phone_number TEXT,
    gender TEXT,
    password TEXT,
    qualification TEXT,
    specialization TEXT,
    registration_number TEXT
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    patient_name TEXT,
    patient_id INTEGER,
    doctor_name TEXT,
    appointment_date DATE,
    appointment_time TIME,
    reason TEXT NOT NULL,
    symptoms TEXT NOT NULL,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY (patient_id) REFERENCES registered_patient(id)
);