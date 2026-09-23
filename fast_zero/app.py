from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title='FASTZERO', host='0.0.0.0', port=8000, reload=True)


database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/lista', response_class=HTMLResponse, status_code=HTTPStatus.CREATED)
def manda_html():
    return '<h1>Lista-1</h1>'


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            detail='Não encontrou o usuario no DB da memória',
            status_code=HTTPStatus.NOT_FOUND,
        )
    return user_with_id


@app.delete(
    'users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            detail='Não encontrou o usuario no DB da memória',
            status_code=HTTPStatus.NOT_FOUND,
        )

    return database.pop(user_id=1)
