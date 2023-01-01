from fastapi import Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from models.cliente import *

router = APIRouter()

@router.post("/api/clientes", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def create(request: ClienteRequest, db: Session = Depends(get_db)):
    cliente = ClienteRepository.save(db, Cliente(**request.dict()))
    return ClienteResponse.from_orm(cliente)

@router.get("/api/clientes", response_model=list[ClienteResponse])
def find_all(db: Session = Depends(get_db)):
    clientes = ClienteRepository.find_all(db)
    return [ClienteResponse.from_orm(cliente) for cliente in clientes]

@router.get("/api/clientes/id/{id}", response_model=ClienteResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    cliente = ClienteRepository.find_by_id(db, id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    return ClienteResponse.from_orm(cliente)

@router.get("/api/clientes/nome/{nome}", response_model=list[ClienteResponse])
def find_by_nome(nome: str, db: Session = Depends(get_db)):
    clientes = ClienteRepository.find_by_nome(db, nome)
    return [ClienteResponse.from_orm(cliente) for cliente in clientes]

@router.delete("/api/clientes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ClienteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    ClienteRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/clientes/{id}", response_model=ClienteResponse)
def update(id: int, request: ClienteRequest, db: Session = Depends(get_db)):
    if not ClienteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    cliente = ClienteRepository.save(db, Cliente(id=id, **request.dict()))
    return ClienteResponse.from_orm(cliente)
