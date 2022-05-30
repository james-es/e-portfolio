from healthcare_professional import Nurse, Doctor
from patient import Patient
from receptionist import Receptionist

# The receptionist represents the receptionist at the clinic
receptionist = Receptionist("Sarah Smith", "RC3003")

# Verify that the receptionist has been created
print(
    f"a receptionist has been created with name {receptionist.name} and employee number {receptionist.employee_number}")

# Verify that the appointment schedule has been created as well.
# (when a receptionist is created, a new schedule is created as well)
print(
    f"the appointment schedule has been created with {len(receptionist.appointment_schedule.appointments)} appointments")

# Create a doctor
doctor = Doctor("William Johnson", "DC1002")

# Create a nurse
nurse = Nurse("Favour Waters", "NU333")

# verify that both the doctor and nurse can perform a consultation
print("doctor", doctor.consultation())
print("nurse", nurse.consultation())

# a patient walks into the clinic
patient = Patient("Hermione Jean", "15, Privet Drive", "336726489")

# the patient tells the receptionist to schedule an appointment with Mr William
appointment = patient.request_appointment(doctor, receptionist)

# verify that the appointment has been scheduled
print(f"the appointment schedule now contains {len(receptionist.appointment_schedule.appointments)} appointments")


# the appointment time is now and the patient visits the receptionist.
# the receptionist checks to find the next appointment
nextAppointment = receptionist.appointment_schedule.find_next_available()

# The receptionist verifies the patient's name and lets the patient see the doctor
print(f"The next appointment is {nextAppointment.patient.name}")

# the doctor issues the prescription
prescription = doctor.issue_prescription("Drugs", patient, 3, 2)

# verify the prescription
print(f"A prescription has been created by Doctor {prescription.doctor.name}. Type {prescription.type}, Patient's name {prescription.patient.name}, Quantity {prescription.quantity}, Dosage {prescription.dosage}")


# the reception cancels the appointment since the patient has seen the doctor
receptionist.appointment_schedule.cancel_appointment(nextAppointment)

# verify that the schedule is now empty
print(f"the appointment schedule now contains {len(receptionist.appointment_schedule.appointments)}")