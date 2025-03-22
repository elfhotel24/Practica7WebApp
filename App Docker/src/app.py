from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos (SQLite)
DATABASE_URL = "sqlite:///./test.db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Definir el modelo de la tabla
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(255), nullable=False)

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

# Modelo Pydantic para la respuesta
class MessageResponse(BaseModel):
    id: int
    message: str

# Ruta para obtener el mensaje
@app.get("/", response_model=MessageResponse)
def read_message():
    db = SessionLocal()
    message = db.query(Message).first()
    db.close()
    if message is None:
        raise HTTPException(status_code=404, detail="No hay mensajes en la base de datos")
    return message