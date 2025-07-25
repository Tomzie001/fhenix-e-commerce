from fastapi import FastAPI
from .api import user_management, product_management
from sqlmodel import SQLModel 
from .database import engine
from fastapi.middleware.cors import CORSMiddleware



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app= FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
 

app.include_router(user_management.router)
app.include_router(product_management.router) 

# creating all tables 
# turning on our server
# includes all routes(api folder)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)