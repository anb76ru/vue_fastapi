import json
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from models import User, UserAdult
from database import MongoDB

fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]


class Item(BaseModel):
    num1: int
    num2: int


user = User(**{"name": "John Doe", "id": 1})

app = FastAPI()


@app.get("/hw")
async def root():
    return {"message": "Сова сипуха"}


@app.get("/calculate")
async def calculate():
    return {"message": "Вычислить сумму двух чисел"}


@app.post("/get-sum")
@app.options("/get-sum", status_code=200)
async def get_summ(body: Item):
    return {"result": body.num1 + body.num2}


@app.get("/user")
async def get_user():
    return user.model_dump()


@app.post("/user")
async def is_adult(user_adult: UserAdult):
    data = user_adult.model_dump()
    data.update({'is_adult': data.get('age') > 18})
    return data


@app.get("/user/{user_id}")
async def get_user_id(user_id: int):
    return {"вы просили найти юзера с id": user_id}

@app.get("/users")
async def get_users():
    return list(MongoDB.db.users.find({}, {"username": 1, "user_info": 1, "_id": 0}))
    #return fake_db

class SearchUser(BaseModel):
    username: str

@app.post("/search-users")
def search_users(username: SearchUser):
    return list(MongoDB.db.users.find({"username": username.username}, {"username": 1, "user_info": 1, "_id": 0}))



if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", reload=True, headers=[("Access-Control-Allow-Origin", "*"),
                                                                    ("Access-Control-Request-Method", "*"),
                                                                    ("Access-Control-Allow-Methods", "*"),

                                                                    ("Access-Control-Allow-Headers", "Content-Type")])