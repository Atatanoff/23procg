from sqlalchemy import Column, Integer, LargeBinary
from database import Base
from sqlalchemy.orm import relationship


class Icons(Base):
    __tablename__ = 'icons'
    id = Column(Integer, primary_key=True, index=True)
    icons = Column(LargeBinary)
    macros = relationship('Macros', back_populates='icon')
    
    