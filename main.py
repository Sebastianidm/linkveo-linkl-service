from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from typing import List # Para devolver una lista de links
import models
import schemas
import crud
import security 
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Servicio de Links")

# --- ENDPOINT PARA CREAR UN LINK (PROTEGIDO) ---
@app.post("/links", response_model=schemas.Link, status_code=status.HTTP_201_CREATED)
def create_link_for_user(
    link: schemas.LinkCreate,
    db: Session = Depends(get_db),
    owner_id: int = Depends(security.get_current_user_id) 
):
    """
    Crea un nuevo link para el usuario autenticado.
    """
    return crud.create_user_link(db=db, link=link, owner_id=owner_id)


# --- ENDPOINT PARA LEER LINKS (PROTEGIDO) ---
@app.get("/links", response_model=List[schemas.Link])
def read_links_for_user(
    db: Session = Depends(get_db),
    owner_id: int = Depends(security.get_current_user_id) # <-- MAGIA AQUÍ
):
    """
    Devuelve la lista de links del usuario autenticado.
    """
    links = crud.get_links_by_owner(db, owner_id=owner_id)
    return links