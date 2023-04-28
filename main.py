from fastapi import FastAPI


from fastapi.params import Body


from pydantic import BaseModel

from typing import Optional
from main import my_post


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str

    isPublished: bool = True

    rating: Optional[int] = None


my_post = [{"title:" "title of post 1", "content:" "content of post 1", "id:" "1"}, {
    "title:" "title of post 2", "content:" "content of post 2", "id:" "2"}]


@app.get("/")
async def root():

    return {"message": "Welcome to my api"}


@app.get("/posts")
def get_post():

    return {"data": my_post}


@app.post("/posts")
def create_post(post: Post):
    print(post.dict())

    return {"data": post}
