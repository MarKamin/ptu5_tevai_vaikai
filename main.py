from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/tevai_vaikai.db')
Base = declarative_base()

import random
from sty import fg

def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red,green,blue

def generateColor(red,green,blue):
    return fg(red,green,blue)

red,green,blue = generateRGB()
color = generateColor(red,green,blue)
print(color, 'HiHiHi')

class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde})"

class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    mokymo_istaiga = Column("mokykla", String, nullable=True)
    # ForeignKey veda i lenteles pavadinima
    tevas_id = Column("tevas_id", Integer, ForeignKey("tevas.id")) # duomenu bazej
    # lenteles pavadinimas, ne bojekto (vietoj tevas.id) jeigu butume susukiure tablename
    # Relationship veda i objekto pavadinima (pythonui)
    tevas = relationship("Tevas")

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde} {self.tevas})"

if __name__ == "__main__":
   # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

