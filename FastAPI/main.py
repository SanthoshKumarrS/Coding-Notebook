from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

my_posts = [{"title": "First Post", "content": "This is the first post.", "id": 1},
             {"title": "Second Post", "content": "This is the second post.", "id": 2}]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Welcome to my API!"}


@app.get("/posts")
def get_posts():
    return [{"Data": my_posts}]


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"newpost": post_dict}



