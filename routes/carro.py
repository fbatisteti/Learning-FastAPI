from fastapi import Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from models.carro import *

router = APIRouter()

@router.post("/api/carros", response_model=CarroResponse, status_code=status.HTTP_201_CREATED)
def create(request: CarroRequest, db: Session = Depends(get_db)):
    carro = CarroRepository.save(db, Carro(**request.dict()))
    return CarroResponse.from_orm(carro)

@router.get("/api/carros", response_model=list[CarroResponse])
def find_all(db: Session = Depends(get_db)):
    carros = CarroRepository.find_all(db)
    return [CarroResponse.from_orm(carro) for carro in carros]

@router.get("/api/carros/id/{id}", response_model=CarroResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    carro = CarroRepository.find_by_id(db, id)
    if not carro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Carro não encontrado"
        )
    return CarroResponse.from_orm(carro)

@router.get("/api/carros/placa/{placa}", response_model=list[CarroResponse])
def find_by_placa(placa: str, db: Session = Depends(get_db)):
    carros = CarroRepository.find_by_placa(db, placa)
    return [CarroResponse.from_orm(carro) for carro in carros]

@router.get("/api/carros/porte/{porte}", response_model=list[CarroResponse])
def find_by_placa(porte: str, db: Session = Depends(get_db)):
    carros = CarroRepository.find_by_porte(db, porte)
    return [CarroResponse.from_orm(carro) for carro in carros]

@router.get("/api/carros/modelo/{modelo}", response_model=list[CarroResponse])
def find_by_placa(modelo: str, db: Session = Depends(get_db)):
    carros = CarroRepository.find_by_modelo(db, modelo)
    return [CarroResponse.from_orm(carro) for carro in carros]

@router.delete("/api/carros/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CarroRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Carro não encontrado"
        )
        
    CarroRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/carros/{id}", response_model=CarroResponse)
def update(id: int, request: CarroRequest, db: Session = Depends(get_db)):
    if not CarroRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Carro não encontrado"
        )
    carro = CarroRepository.save(db, Carro(id=id, **request.dict()))
    return CarroResponse.from_orm(carro)
