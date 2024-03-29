# https://www.youtube.com/watch?v=0zb2kohYZIM&t=634s

from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse, RedirectResponse


import models
import schemas
from database import engine, get_db


app = FastAPI()

# CORS

origins = [
    "http://localhost:3000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# инъекция зависимостей с аннотациями
db_dependency = Annotated[Session, Depends(get_db)]

# создаем БД со всеми таблицами, когда создается приложение FastAPI
models.Base.metadata.create_all(bind=engine)




# сервисы, функции

import service




# маршруты


app.mount("/static", StaticFiles(directory="./front/build/static"), name="static")


@app.get("/", response_class=FileResponse)
def index():
    root = 'front/build/index.html'
    return FileResponse(root)


@app.get('/test/')
async def test():
    print('test')
    return service.get_home()


@app.get('/file_list/')
async def file_list():
    return service.get_list_file_and_dir()






# ...response_model=TransactionModel - схема (шаблон) ответа соответсвует схеме запроса
# @app.post('/transactions/', response_model=TransactionModel)
# async def create_transaction(transaction: TransactionBase, db: db_dependency):
#     print(type(transaction))
#     db_transaction = models.Transaction(**transaction.dict())
#     db.add(db_transaction)
#     db.commit()
#     db.refresh(db_transaction)
#     return db_transaction


# @app.get('/')
# def root():
#     html_content = """
#     <html>
#         <head>
#             <title>Brownie</title>
#         </head>
#         <body>
#             <h4>Добро пожаловать в систему умного дома <span style="color: red">brownie</span></h4>
#         </body>
#     </html>
#     """
#     return HTMLResponse(content=html_content, status_code=200)





# if __name__ == "__main__":
#     uvicorn.run(
#         app,
#         # host="0.0.0.0",
#         # port=8000
#     )
