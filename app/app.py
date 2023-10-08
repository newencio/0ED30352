from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from app.database.db import DB
from app.models.error import NotFoundException
from app.models import AddDoctorRequest
from app.services.availability_service import AvailabilityService
from app.services.doctor_service import DoctorService, InDatabaseDoctorService, InMemoryDoctorService
from app.settings import Settings


def create_app() -> FastAPI:
    doctor_service: DoctorService
    available_service: AvailabilityService
    db: Optional[DB] = None
    if Settings.in_database:
        db = DB()
        db.init_if_needed()
        doctor_service = InDatabaseDoctorService(db=db)
        available_service = AvailabilityService(db=db)
    else:
        doctor_service = InMemoryDoctorService()
        doctor_service.seed()

    app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})

    @app.get('/doctors')
    def list_doctors():
        return doctor_service.list_doctors()

    @app.get('/doctors/{id}')
    async def get_doctor(id: int):
        return doctor_service.get_doctor(id)

    @app.post('/doctors')
    def add_doctor(request: AddDoctorRequest):
        id = doctor_service.add_doctor(first_name=request.first_name, last_name=request.last_name)
        return {
            'id': id
        }

    @app.get('/doctors/{doctor_id}/locations')
    def get_doctor_locations(doctor_id: int):
        return doctor_service.list_doctor_locations(doctor_id=doctor_id)

    # Add new endpoints here! #
    @app.post("/schedule/")
    def add_schedule(doctor_id: int, day_of_week: str, start_time: str, end_time: str):
        return available_service.add_schedule(doctor_id, day_of_week, start_time, end_time)

    @app.get("/schedule/{doctor_id}")
    def get_schedule(doctor_id: int):
        return available_service.get_schedule(doctor_id)

    @app.post("/appointment/")
    def book_appointment(doctor_id: int, location_id: int, appointment_time: str, duration: int):
        appointment_time_dt = datetime.strptime(appointment_time, '%Y-%m-%dT%H:%M:%S')
        return available_service.book_appointment(doctor_id, location_id, appointment_time_dt, duration)

    @app.get("/appointments/{doctor_id}")
    def get_appointments(doctor_id: int):
        return available_service.get_appointments(doctor_id)

    @app.delete("/appointment/{appointment_id}")
    def cancel_appointment(appointment_id: int):
        available_service.cancel_appointment(appointment_id)
        return {"status": "cancelled"}

    @app.get("/availability/{doctor_id}")
    def get_availability(doctor_id: int, start_date: str, end_date: str):
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        return available_service.get_availability(doctor_id, start_date_dt, end_date_dt)

    @app.exception_handler(NotFoundException)
    async def not_found(request: Request, exc: NotFoundException):
        return Response(status_code=404)

    @app.on_event('shutdown')
    def shutdown():
        if db:
            db.close_db()

    @app.get('/', include_in_schema=False)
    def root():
        return RedirectResponse('/docs')

    return app


app = create_app()
