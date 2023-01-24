from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None



my_posts = []


@app.get("/")
def root():
    return {"message": "Welcome to my api !!!"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
 #title str, content str,


