

from app.database.db import DB


from datetime import datetime, timedelta
from typing import List, Tuple, Optional, Dict, Any


class AvailabilityService:

    def __init__(self, db: DB):
        self.db = db

    def add_schedule(self, doctor_id: int, day_of_week: str, start_time: str, end_time: str) -> list[dict[str, Any]]:
        return self.db.execute(
            "INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES (?, ?, ?, ?)",
            (doctor_id, day_of_week, start_time, end_time)
        )

    def get_schedule(self, doctor_id: int) -> list[dict[str, Any]]:
        return self.db.execute(
            "SELECT day_of_week, start_time, end_time FROM schedules WHERE doctor_id = ?",
            (doctor_id,)
        )

    def book_appointment(self, doctor_id: int, location_id: int, appointment_time: datetime, duration: int = 30) -> int:
        end_time = appointment_time + timedelta(minutes=duration)

        # Check if the doctor is already booked within the requested time range
        existing_appointments = self.db.execute(
            "SELECT appointment_time, duration FROM appointments WHERE doctor_id = ? AND NOT (appointment_time + duration * 60 < ? OR appointment_time > ?)",
            (doctor_id, appointment_time.timestamp(), end_time.timestamp())
        )

        if existing_appointments:
            raise Exception("Doctor is already booked within the requested time range")

        # Insert the new appointment
        self.db.execute(
            "INSERT INTO appointments (doctor_id, location_id, appointment_time, duration) VALUES (?, ?, ?, ?)",
            (doctor_id, location_id, appointment_time.strftime('%Y-%m-%d %H:%M:%S'), duration)
        )

        # Add any further logic here if needed

        return "Appointment successfully booked."

    def get_appointments(self, doctor_id: int) -> List[Tuple[int, str, datetime]]:
        return self.db.execute(
            "SELECT id, location_id, appointment_time FROM appointments WHERE doctor_id = ?",
            (doctor_id,)
        )

    def cancel_appointment(self, appointment_id: int) -> None:
        self.db.execute(
            "DELETE FROM appointments WHERE id = ?",
            (appointment_id,)
        )

    def get_availability(self, doctor_id: int, start_date: datetime, end_date: datetime) -> List[Tuple[str, datetime]]:
        schedule = self.get_schedule(doctor_id)

        existing_appointments = self.db.execute(
            "SELECT appointment_time FROM appointments WHERE doctor_id = ? AND appointment_time BETWEEN ? AND ?",
            (doctor_id, start_date.strftime('%Y-%m-%d %H:%M:%S'), end_date.strftime('%Y-%m-%d %H:%M:%S'))
        )
        booked_times = set(appointment[0] for appointment in existing_appointments)

        availability = []
        current_date = start_date
        while current_date <= end_date:
            day_of_week = current_date.strftime('%A')
            for s_day_of_week, s_start_time, s_end_time in schedule:
                if day_of_week == s_day_of_week:
                    start_dt = datetime.strptime(f"{current_date.strftime('%Y-%m-%d')} {s_start_time}",
                                                 '%Y-%m-%d %H:%M:%S')
                    end_dt = datetime.strptime(f"{current_date.strftime('%Y-%m-%d')} {s_end_time}", '%Y-%m-%d %H:%M:%S')

                    current_time = start_dt
                    while current_time < end_dt:
                        if current_time.strftime('%Y-%m-%d %H:%M:%S') not in booked_times:
                            availability.append((day_of_week, current_time))
                        current_time += timedelta(minutes=30)  # Assuming 30-minute slots for simplicity

            current_date += timedelta(days=1)

        return availability
