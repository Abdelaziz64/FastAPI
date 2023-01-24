
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Welcome to my api !!!"}

@app.get("/posts")
def get_posts():
    return {"data":"this is your post"}

@app.post("/createposts")
def create_post(post: Post):
    print(post)
    return{"data":"new post"}
 #title str, content str,


