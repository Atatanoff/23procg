from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import res


engine = create_engine("sqlite:///"+res.data, echo=True)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)
