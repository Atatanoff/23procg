from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class MacrosWrite(Base):
    __tablename__ = 'macros_write'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    macros = Column(String)
    button = relationship('Buttons', back_populates='macros_write')



