#Se encarga de la conexion a la base de datos
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Denifimos la URL de la base de datos (SQLite en este caso)
SQLITE_DATABASE_URL = "sqlite:///./links.db"

#Creamos el motor de la base de datos
engine = create_engine(
    SQLITE_DATABASE_URL, connect_args={"check_same_thread": False}
)


#Creamos una fabrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Creamos una Base para nuestros modelos
Base = declarative_base()

#Dependencia para obtener la sesion de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()