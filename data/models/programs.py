from sqlalchemy import Column, Integer, String
from data.database import Base
from sqlalchemy.orm import relationship


class Programs(Base):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    color = Column(String)
    macros = relationship('Macros', back_populates='programs')
    button = relationship('Buttons', back_populates='programs')