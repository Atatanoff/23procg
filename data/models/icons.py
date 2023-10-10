from sqlalchemy import Column, Integer, LargeBinary, String
from data.database import Base
from sqlalchemy.orm import relationship


class Icons(Base):
    __tablename__ = 'icons'
    id = Column(Integer, primary_key=True, index=True)
    icons = Column(LargeBinary)
    mode = Column(String)
    width = Column(Integer)
    hight = Column(Integer)
    macros = relationship('Macros', back_populates='icons')
    button = relationship('Buttons', back_populates='icons')
    
    