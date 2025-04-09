from pydantic import BaseModel

class Flight(BaseModel):
    source_iata: str 
    target_iata: str
    return_date: str
    