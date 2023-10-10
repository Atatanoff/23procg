from sqlalchemy import Column, Integer, String, ForeignKey
from data.database import Base
from sqlalchemy.orm import relationship

class Buttons(Base):
    __tablename__ = 'buttons'
    id = Column(Integer, primary_key=True, index=True)
    buttons = Column(String)
    name = Column(String)
    activity = Column(String)
    icon_id = Column(Integer, ForeignKey('icons.id'))
    program_id = Column(Integer, ForeignKey('programs.id'))
    icon = relationship('Icons', back_populates='buttons')
    program = relationship('Programs', back_populates='buttons')
