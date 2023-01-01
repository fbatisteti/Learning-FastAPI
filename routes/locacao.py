from fastapi import Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from models.locacao import *

router = APIRouter()

@router.post("/api/locacoes", response_model=LocacaoResponse, status_code=status.HTTP_201_CREATED)
def create(request: LocacaoRequest, db: Session = Depends(get_db)):
    locacao = LocacaoRepository.save(db, Locacao(**request.dict()))
    return LocacaoResponse.from_orm(locacao)

@router.get("/api/locacoes", response_model=list[LocacaoResponse])
def find_all(db: Session = Depends(get_db)):
    locacoes = LocacaoRepository.find_all(db)
    return [LocacaoResponse.from_orm(locacao) for locacao in locacoes]

@router.get("/api/locacoes/id/{id}", response_model=LocacaoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    locacao = LocacaoRepository.find_by_id(db, id)
    if not locacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Locação não encontrada"
        )
    return LocacaoResponse.from_orm(locacao)

@router.get("/api/locacoes/carro/{id}", response_model=list[LocacaoResponse])
def find_by_carro(db: Session = Depends(get_db)):
    locacoes = LocacaoRepository.find_by_carro(db, id)
    return [LocacaoResponse.from_orm(locacao) for locacao in locacoes]

@router.get("/api/locacoes/cliente/{id}", response_model=list[LocacaoResponse])
def find_by_cliente(db: Session = Depends(get_db)):
    locacoes = LocacaoRepository.find_by_cliente(db, id)
    return [LocacaoResponse.from_orm(locacao) for locacao in locacoes]

@router.get("/api/locacoes/retirada/{retirada}", response_model=list[LocacaoResponse])
def find_by_retirada(retirada: str, db: Session = Depends(get_db)):
    locacoes = LocacaoRepository.find_by_retirada(db, retirada)
    return [LocacaoResponse.from_orm(locacao) for locacao in locacoes]

@router.get("/api/locacoes/devolucao/{devolucao}", response_model=list[LocacaoResponse])
def find_by_devolucao(devolucao: str, db: Session = Depends(get_db)):
    locacoes = LocacaoRepository.find_by_devolucao(db, devolucao)
    return [LocacaoResponse.from_orm(locacao) for locacao in locacoes]

@router.delete("/api/locacoes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not LocacaoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Locação não encontrada"
        )
    LocacaoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/locacoes/{id}", response_model=LocacaoResponse)
def update(id: int, request: LocacaoRequest, db: Session = Depends(get_db)):
    if not LocacaoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Locação não encontrada"
        )
    locacao = LocacaoRepository.save(db, Locacao(id=id, **request.dict()))
    return LocacaoResponse.from_orm(locacao)
