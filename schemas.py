#Contrato de datos para el servicio de links
from pydantic import BaseModel, HttpUrl

class LinkBase(BaseModel):
    title: str
    url: HttpUrl #Valida que sea una URL correcta

#Esquema creacion de link
class LinkCreate(LinkBase):
    pass

#Esquema de lectura de link
class Link(LinkBase):
    id: int
    owner_id: int
    #Configura el modelo para trabajar con ORM
    class Config:
        from_attributes = True

    
