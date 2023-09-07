from sqlalchemy import Column, Integer, String, ForeignKey
from data.database import Base
from sqlalchemy.orm import relationship


class Macros(Base):
    __tablename__ = 'macros'
    id = Column(Integer, primary_key=True, index=True)
    macros = Column(String)
    name = Column(String)
    icon_id = Column(Integer, ForeignKey('icons.id'))
    icon = relationship('Icons', back_populates='macros')
    program_id = Column(Integer, ForeignKey('programs.id'))
    program = relationship('Programs', back_populates='macros')
    button = relationship('Buttons', back_populates='macros')