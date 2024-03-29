import models
from schemas import *
from main import db_dependency
from database import SessionLocal


def add_user(user: UserBase, db: db_dependency):
    print(user)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


def get_user(db: db_dependency = SessionLocal()):
    users = db.query(models.User).all()
    return users


def add_home(home: HomeBase, db: db_dependency = SessionLocal()):
    new_home = models.Home(**home.dict())
    db.add(new_home)
    db.commit()
    db.refresh(new_home)


def get_home(db: db_dependency = SessionLocal()):
    houses = db.query(models.Home).all()
    return houses



# new_home = HomeBase(
#     name='Тонкинская, 1А',
#     description='основная квартира'
# )
#
# add_home(new_home)



# add_user(
#     UserBase(
#         firstname='Alex',
#         lastname='Pupkin',
#         email='pupkin@mail.ru',
#
#         is_active=True,
#         login='alex',
#         pwd='123',
#
#         houses=SessionLocal().query(models.Home).first()
#
#     ),
#     SessionLocal()
# )



# print('Home', get_home()[0].user_id)
user = SessionLocal().query(models.Home).first()
print(user)
print('User: ', get_user()[0].houses)


import pathlib
def get_list_file_and_dir():
    file = [p for p in pathlib.Path('.').iterdir() if p.is_file()]
    dir = [p for p in pathlib.Path('.').iterdir() if p.is_dir()]
    return {'files': file, 'dirs': dir}

print(type(get_list_file_and_dir()['files'][0]))