from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

class UserAdult(BaseModel):
    name: str
    age: int

