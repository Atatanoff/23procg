from sqlalchemy import Column, Integer, String, ForeignKey
from data.database import Base
from sqlalchemy.orm import relationship

class Buttons(Base):
    __tablename__ = 'buttons'
    id = Column(Integer, primary_key=True, index=True)
    buttons = Column(String)
    name = Column(String)
    activity = Column(String)
    macros_id = Column(Integer, ForeignKey('macros.id'))
    macros = relationship('Macros', back_populates='button')
