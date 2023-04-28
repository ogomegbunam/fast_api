from fastapi import FastAPI


from fastapi.params import Body


from pydantic import BaseModel

from typing import Optional


app = FastAPI()



class Post(BaseModel):
    title: str
    content: str


    isPublished: bool = True

    rating: Optional[int] = None



@app.get("/")


async def root():


    return {"message": "Welcome to my api"}




@app.get("/get_post")


def get_post():


    return {"data": "This is your post"}


@app.post("/createpost")


def create_post(post: Post):
    print(post.dict())

    return{"data":post}