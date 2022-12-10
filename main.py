from typing import List

import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.matrix import matrix_transpose

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app_name = "Math Buddyz"
version = 0.1


@app.get("/")
async def read_item():
    return {
        "check": "Ok"
    }


@app.get("/health")
async def health():
    return {
        "name": app_name,
        "version": version
    }


@app.post("/matrix_transpose/")
async def matrix_transpose_api(MatrixDict: dict):
    """ matrix_transpose
    MatrixDict: {
        "matrix": [Nested Array]
    }
    """
    if len(MatrixDict["matrix"]) != 0:
        return {
            "result": matrix_transpose(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)
