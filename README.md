# **Simple FastAPI example**

## **About**

This is a simple FastAPI example, based on [this tutorial by Cleyson Lima](https://www.treinaweb.com.br/blog/criando-o-primeiro-crud-com-fastapi) but with a lot of modifications to fit another theme, for a car rental company.

All data already in inputted in the SQLite database was made with mock-ups from [4devs](https://www.4devs.com.br/). Any similarity with real-world people and/or cars is mere coincidence.

## **Dependencies**
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## **Video Explanation of the Project**
[Redirect to YouTube](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

## **General Explanation of the Project**

### CLASSES

I tried to make it  short and simple. The entire API runs with three classes, namely "Carro", "Cliente" and "Locacao" (Car, Customer, Rental, respectively). Each have some attributes (which will also be their tables' columns), as shown below:

### Carro (Car)
- ID
- Placa (License plate)
- Porte (Size)
- Modelo (Model)

### Cliente (Customer)
- ID
- Nome (Name)

### Locacao (Rental)
- ID
- Carro_ID (Car_ID)
- Cliente_ID (Customer_ID)
- Retirada (Date of rental)
- Devolucao (Date of return)

All classes/tables will have all basic HTTP requests (GET, POST, PUT and DELETE), with some minor variations to account for the future need of specific searches.

### PROJECT SETUP AND HOSTING

Setup the project with the following commands:
```
python -m venv .venv   
.\.venv\Scripts\activate  
```
Then you can host it with:
```
uvicorn main:app --reload
```
If you want to host on a specific port, add *--port PORT* to the line above, changing PORT to your desired one. By default, port 8000 will be used.

You can check the documentation generated by FastAPI <font size="1">(heaven sent feature, IMO)</font> on [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)



