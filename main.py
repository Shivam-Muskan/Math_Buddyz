from typing import List

import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.matrix import matrix_transpose, multiple_matrix_multiply, multiple_matrix_addition, matrix_det, \
    matrix_inverse, matrix_adjoint

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
            print("\n \n \n \n Final Result:",result)
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


@app.post("/matrix_determinant/")
async def matrix_determinant_api(MatrixDict: dict):
    """ matrix_determinant
    MatrixDict: {
        "matrix": [Nested Array]
    }
    """
    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        result = matrix_det(MatrixDict["matrix"])
        if result is not None:
            return {
                "result": result
            }
        return {"error": True, "message": "Not a Square Matrix. Determinant cannot be found."}
    return {"error": True, "message": "Invalid matrix."}

@app.post("/matrix_inverse/")
async def matrix_inverse_api(MatrixDict: dict):
    """ matrix_determinant
    MatrixDict: {
        "matrix": [Nested Array]
    }
    """
    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        result, determinant, error = matrix_inverse(MatrixDict["matrix"])
        if result is not None:
            return {
                "determinant": determinant,
                "result": result
            }
        return {"error": True, "message": error}
    return {"error": True, "message": "Invalid matrix."}


@app.post("/matrix_adjoint/")
async def matrix_adjoint_api(MatrixDict: dict):
    """ matrix_adjoint
    MatrixDict: {
        "matrix": [Nested Array]
    }
    """
    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "result": matrix_adjoint(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
