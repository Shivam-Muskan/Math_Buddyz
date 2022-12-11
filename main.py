from typing import List

import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.matrix import matrix_transpose, multiple_matrix_multiply, multiple_matrix_addition

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
    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "result": matrix_transpose(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}


@app.post("/matrix_multiplication/")
async def matrix_multiplication_api(MatrixDict: dict):
    """
    :param MatrixDict: {
    "matrix":[Nested Array]
    }
    :return:
    """

    matrices = MatrixDict.get('matrix')
    total_matrices = len(matrices)
    if matrices and total_matrices >= 2:
        result = multiple_matrix_multiply(MatrixDict['matrix'], total_matrices)
        if result is not None:
            return {
                "result": result
            }
    return {"error": True, "message": "Invalid parameters."}


@app.post("/matrix_addition/")
async def matrix_addition_api(MatrixDict: dict):
    """
    :param MatrixDict: {
    "matrix":[Nested Array]
    }
    :return:
    """

    matrices = MatrixDict.get('matrix')
    total_matrices = len(matrices)

    if matrices and total_matrices >= 2:
        result = multiple_matrix_addition(MatrixDict['matrix'], total_matrices)
        if result is not None:
            return {
                "result": result
            }
    return {"error": True, "message": "Invalid parameters."}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
