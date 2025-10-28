from sqlalchemy.orm import Session
import models
import schemas

def get_links_by_owner(db: Session, owner_id: int):
    #Buscamos los links por owner_id
    return db.query(models.Link).filter(models.Link.owner_id == owner_id).all()

def create_user_link(db: Session, link: schemas.LinkCreate, owner_id: int):
    # Creamos el objeto del modelo SQLAlchemy
    db_link = models.Link(
        title=link.title,
        url=str(link.url), # Convertimos la URL de Pydantic a string
        owner_id=owner_id
    )

    # Agregamos el nuevo link a la sesión de la base de datos
    db.add(db_link)
    db.commit()
    db.refresh(db_link)

    return db_link

