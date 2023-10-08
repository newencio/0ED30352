from typing import List

from pydantic import BaseModel


class AddDoctorRequest(BaseModel):
    first_name: str
    last_name: str
    locations: List[str] = []
