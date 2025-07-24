from .database import get_session
from fastapi import Depends
from sqlmodel import Session
from typing import Annotated


dbconn = Annotated[Session,Depends(get_session)]