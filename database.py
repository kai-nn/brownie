from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:hydrapostgres@localhost:5432/brownie'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# зависимость от БД
def get_db():
    # db = копия БД на время сеанса
    db = SessionLocal()
    try:
        # получаем доступ к БД только при поступлении запроса
        yield db
    finally:
        # при любом исходе закрываем доступ к БД
        db.close()


