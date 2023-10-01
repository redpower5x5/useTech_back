from typing import Union, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from generators.gen_simple_styled import GenStyledProject
from generators.gen_simple_css import GenCSSProject
import uuid
import base64
import os

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Compile_data(BaseModel):
    style: str
    data: str


@app.get("/download/{uuid}")
async def download_generated_zip(uuid: str):
    # check if file exists
    if not os.path.isfile(f"compiled/{uuid}.zip"):
        return {'error': 'file not found'}
    else:
        return FileResponse(f"compiled/{uuid}.zip", media_type="application/zip", filename="generated_code.zip")

@app.post("/compile/")
async def compile_project(compile_data: Compile_data):
    decoded = base64.b64decode(compile_data.data).decode("utf-8")
    if compile_data.style == "css":
        gen = GenCSSProject(decoded)
        gen.insert_data_into_files()
        id = str(uuid.uuid4())
        gen.zip_project(id)
        return {'uuid': id}
    elif compile_data.style == "styled":
        gen = GenStyledProject(decoded)
        gen.insert_data_into_files()
        id = str(uuid.uuid4())
        gen.zip_project(id)
        return {'uuid': id}
    else:
        return {'error': 'invalid style'}