from typing import Optional

from fastapi import FastAPI
from fastapi import Response, HTTPException, status
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


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] ==id:
            return i
        
@app.get("/")
async def root():
    return {"message": "Welcome to my API!"}


@app.get("/posts")
def get_posts():
    return [{"Data": my_posts}]


@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"newpost": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found.")
        
    return {"post_detail": post}


@app.delete("/posts/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id: {id} was not found")
    my_posts.pop(index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail = f"Post with id: {id} was not found")

    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"updated_post": post_dict}