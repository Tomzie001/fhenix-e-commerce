from passlib.context import CryptContext
import jwt


SECRET_KEY = "6b639071dc04f81bc50b046b5ab95ec4c21b272449238eeea14ba254cb09ded9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    print(pwd_context.hash(password))
    return pwd_context.hash(password)

def jwt_encode(data):
    token= jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def jwt_decode(token):
    data= jwt.encode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return data