from app.utils import get_password_hash, verify_password, jwt_encode
from ..models.user_management import User 
from sqlmodel import select
from fastapi import HTTPException

def createNewUser(session,data):
    statement = select(User).where(User.email == data.email)
    result= session.exec(statement).first()

    if result:
       raise HTTPException(status_code=404, detail="email already exists")    


    hashed_pw = get_password_hash(data.password)
    new_user = User(first_name= data.first_name, last_name= data.last_name, email= data.email, password= hashed_pw, user_type= data.user_type)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    new_data = {
        "first name": data.first_name,
        "last_name": data.last_name,
        "email": data.email,
        "user_type": data.user_type,
        "status": "success"
    }
    return new_data


def loginUser(session,data):
    statement = select(User).where(User.email == data.email)
    filtered_user= session.exec(statement).first()

    if filtered_user:
       password = verify_password(data.password,filtered_user.password)
       if password:
          payload = { 
    "id": filtered_user.id  
}
          token = jwt_encode(payload)
          res = {
             "status": "success".capitalize(),
             "token": token,
             "type" : "bearer"   
                }
          return res
          
          
       else:
           raise  HTTPException(status_code=404, detail="invalid password")
            
    else:
       raise  HTTPException(status_code=404, detail="email does not exist")
       


def forgetUserPwd(session, data):
   statement = select(User).where(User.email == data.email)
   filtered_user= session.exec(statement).first()
   if filtered_user:
      pass
#    send otp code
   else:
      raise  HTTPException(status_code=404, detail="email does not exist")