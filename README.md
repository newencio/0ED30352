# Hospital Appointment System

## Overview

This is a simple hospital appointment system that allows patients to book appointments with doctors. See class `availability_service.py` for the main logic.'

## Features

- CRUD operations for doctors
- Ability to model a doctor's availability
- Ability to book an appointment against a doctor's availability
- Ability to get all appointments for a doctor
- Ability to cancel an appointment with a doctor

## API Endpoints

- `POST /doctors`: Add a new doctor
- `GET /doctors`: Get a list of doctors
- `POST /schedule/`: Add a doctor's schedule
- `GET /schedule/{doctor_id}`: Get a doctor's schedule
- `POST /appointment/`: Book an appointment
- `GET /appointments/{doctor_id}`: Get all appointments for a doctor
- `DELETE /appointment/{appointment_id}`: Cancel an appointment

## Extra questions

There was a request to expand the scope of the service. I answered the question `What are some real-world constraints to booking appointments that would add complexity to this API and how would they impact the design` below:


`Multiple Locations with Travel Time`: If a doctor works at multiple locations and needs time to travel between them, the API would need to account for that when booking appointments.
`Impact`: Would require a more complex availability checking mechanism that includes travel time.

`Variable Duration`: Different types of appointments might require different lengths of time.
`Impact`: The API would need to allow for variable-length appointments, complicating the logic for checking availability.

`Buffer Time`: Doctors might require buffer time between appointments. `Impact`: Adds complexity to the scheduling logic to ensure that no appointments are made during these buffer periods.