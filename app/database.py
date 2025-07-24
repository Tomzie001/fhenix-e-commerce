from sqlmodel import create_engine, Session


DEBUG = True

engine = None

if DEBUG:

    sqlite_file_name = "database.db"
    db_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(db_url, connect_args=connect_args)


else:
    db_url = ""
    engine = create_engine(db_url)

    
    
def get_session():
    with Session(engine) as session:
        yield session

