from fastapi import APIRouter

from .calculator import is_upper_triangular, is_lower_triangular, is_diagonal, is_scaler, is_identity, is_null, \
    is_square,matrix_type

router = APIRouter()



@router.post("/matrix_type/")
async def matrix_type_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "result": matrix_type(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}





'''
@router.post("/is_upper_triangular/")
async def is_upper_triangular_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}
    
    result = is_upper_triangular(MatrixDict["matrix"])

    if len(MatrixDict["matrix"]) != 0:
        if result is not None:
            return {
                "message": "Matrix is Upper Triangular.",
                "result": result
            }
        return {"error":True, "message":"This is not a square matrix."}
    return {"error": True, "message": "Invalid Matrix"}


@router.post("/is_lower_triangular/")
async def is_lower_triangular_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "message": "Matrix is Lower Triangular.",
            "result": is_lower_triangular(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}


@router.post("/is_square/")
async def is_square_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "message": "This is Square Matrix.",
            "result": is_square(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}


@router.post("/is_diagonal/")
async def is_diagonal_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "message": "This is Diagonal Matrix.",
            "result": is_diagonal(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}


@router.post("/is_scaler/")
async def is_scaler_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "message": "This is Scaler Matrix.",
            "result": is_scaler(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}


@router.post("/is_identity/")
async def is_identity_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "message": "This is Identity Matrix.",
            "result": is_identity(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}


@router.post("/is_null/")
async def is_null_api(MatrixDict: dict):
    """
    :param MatrixDict: {
        "matrix": [Nested Array]
    }
    """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        return {
            "message": "This is Null Matrix.",
            "result": is_null(MatrixDict["matrix"])
        }
    return {"error": True, "message": "Invalid Matrix"}

'''

