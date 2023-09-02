from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///data/miniboard.db", echo=True)
Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)
