from fastapi import APIRouter
from ..schemas.user_management import UserCreationVal, loginVal, forgetpwdVal
from ..CRUD.user_management import createNewUser, loginUser, forgetUserPwd
from app.dependency import dbconn

router = APIRouter()


# registration
@router.post("/sign-up")
def registration(user_details:UserCreationVal, session:dbconn):
   new_user= createNewUser(session, user_details)
   return new_user

# login
@router.post("/login")
def login(login_details: loginVal, session:dbconn):
   user= loginUser(session, login_details)
   return user
# forgot password
@router.post("/account/forget-password")
def login(user_email: forgetpwdVal, session:dbconn):
   user= forgetUserPwd(session,user_email)
   return user
