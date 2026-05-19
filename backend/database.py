from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
class base(DeclarativeBase) :
    pass

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() :
    db = Session()
    try :
        yield db
    finally :
        db.close()
