from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import Base

# MODEL
class Carro(Base):
    __tablename__ = "carros"
    
    id: int = Column(Integer, primary_key=True, index=True)
    placa: str = Column(String(7), nullable=False)
    porte: str = Column(String(16), nullable=False)
    modelo: str = Column(String(32), nullable=False)

# REPO
class CarroRepository:
    @staticmethod
    def find_all(db: Session) -> list[Carro]:
        return db.query(Carro).all()

    @staticmethod
    def save(db: Session, carro: Carro) -> Carro:
        if carro.id:
            db.merge(carro)
        else:
            db.add(carro)
        db.commit()
        return carro

    @staticmethod
    def find_by_id(db: Session, id: int) -> Carro:
        return db.query(Carro).filter(Carro.id == id).first()
    
    @staticmethod
    def find_by_placa(db: Session, placa: str) -> Carro:
        search = '%' + placa + '%'
        return db.query(Carro).filter(Carro.placa.ilike(search)).all()
    
    @staticmethod
    def find_by_porte(db: Session, porte: str) -> Carro:
        return db.query(Carro).filter(Carro.porte == porte).all()

    @staticmethod
    def find_by_modelo(db: Session, modelo: str) -> Carro:
        search = '%' + modelo + '%'
        return db.query(Carro).filter(Carro.modelo.ilike(search)).all()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Carro).filter(Carro.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        carro = db.query(Carro).filter(Carro.id == id).first()
        if carro is not None:
            db.delete(carro)
            db.commit()

# SCHEMA (MODELS)
class CarroBase(BaseModel):
    placa: str
    porte: str
    modelo: str

class CarroRequest(CarroBase):
    ...

class CarroResponse(CarroBase):
    id: int

    class Config:
        orm_mode = True
