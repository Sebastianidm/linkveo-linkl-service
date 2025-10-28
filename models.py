#Aqui definire la tabla links
from sqlalchemy import Column, Integer, String
from database import Base

class Link(Base):
    __tablename__ = "links"
    #Columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    #Relacion entre microservicios
    owner_id = Column(Integer, index=True, nullable=False)


