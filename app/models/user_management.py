from sqlmodel import Field, SQLModel
from typing import Optional 

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name : str
    last_name: str
    email: str = Field(unique=True, nullable=False)
    password: str
    user_type: str #(buyer,seller, admin)


class OTP(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user : str
    code: str    