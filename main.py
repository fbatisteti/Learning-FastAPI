from fastapi import FastAPI
from database import engine, Base
from models import carro, cliente, locacao
from routes import carro, cliente, locacao

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(carro.router)
app.include_router(cliente.router)
app.include_router(locacao.router)
