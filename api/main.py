from typing import Union, Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/compile/")
async def compile_project(code_style: Annotated[str, Form()], data: Annotated[str, Form()]):
    return {"data": data}