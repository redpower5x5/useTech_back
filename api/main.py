from typing import Union, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form

app = FastAPI()

class Compile_data(BaseModel):
    style: str
    data: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/compile/")
async def compile_project(compile_data: Compile_data):
    print(compile_data.data)
    return {"data": compile_data.data}