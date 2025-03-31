from pydantic import BaseModel

class Flight(BaseModel):
    origin: str
    destination: str
    departure_date: str
    number_of_passengers: int
