from pydantic import BaseModel

class DataAuth(BaseModel):
    location: str
    sqft: int
    bath: int
    bhk: int