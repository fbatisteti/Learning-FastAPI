from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import Base

# MODEL
class Locacao(Base):
    __tablename__ = "locacoes"
    
    id: int = Column(Integer, primary_key=True, index=True)
    carro_id: int = Column(Integer, nullable=False)
    cliente_id: int = Column(Integer, nullable=False)
    retirada: str = Column(String(10), nullable=False)
    devolucao: str = Column(String(10), nullable=True)

# REPO
class LocacaoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Locacao]:
        return db.query(Locacao).all()

    @staticmethod
    def save(db: Session, locacao: Locacao) -> Locacao:
        if locacao.id:
            db.merge(locacao)
        else:
            db.add(locacao)
        db.commit()
        return locacao

    @staticmethod
    def find_by_id(db: Session, id: int) -> Locacao:
        return db.query(Locacao).filter(Locacao.id == id).first()
    
    @staticmethod
    def find_by_carro(db: Session, carro: int) -> Locacao:
        return db.query(Locacao).filter(Locacao.carro_id == carro).all()
    
    @staticmethod
    def find_by_cliente(db: Session, cliente: int) -> Locacao:
        return db.query(Locacao).filter(Locacao.cliente_id == cliente).all()
    
    @staticmethod
    def find_by_retirada(db: Session, retirada: str) -> Locacao:
        return db.query(Locacao).filter(Locacao.retirada == retirada).all()
    
    @staticmethod
    def find_by_devolucao(db: Session, devolucao: str)  -> Locacao:
        return db.query(Locacao).filter(Locacao.devolucao == devolucao).all()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Locacao).filter(Locacao.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        locacao = db.query(Locacao).filter(Locacao.id == id).first()
        if locacao is not None:
            db.delete(locacao)
            db.commit()

# SCHEMA (MODELS)
class LocacaoBase(BaseModel):
    carro_id: int
    cliente_id: int
    retirada: str
    devolucao: str

class LocacaoRequest(LocacaoBase):
    ...

class LocacaoResponse(LocacaoBase):
    id: int

    class Config:
        orm_mode = True
