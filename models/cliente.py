from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import Base

# MODEL
class Cliente(Base):
    __tablename__ = "clientes"
    
    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(100), nullable=False)

# REPO
class ClienteRepository:
    @staticmethod
    def find_all(db: Session) -> list[Cliente]:
        return db.query(Cliente).all()

    @staticmethod
    def save(db: Session, cliente: Cliente) -> Cliente:
        if cliente.id:
            db.merge(cliente)
        else:
            db.add(cliente)
        db.commit()
        return cliente

    @staticmethod
    def find_by_id(db: Session, id: int) -> Cliente:
        return db.query(Cliente).filter(Cliente.id == id).first()
    
    @staticmethod
    def find_by_nome(db: Session, nome: str) -> Cliente:
        search = '%' + nome + '%'
        return db.query(Cliente).filter(Cliente.nome.ilike(search)).all()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Cliente).filter(Cliente.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        cliente = db.query(Cliente).filter(Cliente.id == id).first()
        if cliente is not None:
            db.delete(cliente)
            db.commit()

# SCHEMA (MODELS)
class ClienteBase(BaseModel):
    nome: str

class ClienteRequest(ClienteBase):
    ...

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        orm_mode = True
