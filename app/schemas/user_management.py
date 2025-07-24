from pydantic import BaseModel, EmailStr, Field


class UserCreationVal(BaseModel):
    first_name: str
    last_name: str
    email: str 
    password: str = Field(min_length=4)
    user_type: str #(buyer,seller, admin)


    
class loginVal(BaseModel):
    email: str 
    password: str 
  
  
    
class forgetpwdVal(BaseModel):
    email: EmailStr
 