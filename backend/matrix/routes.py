from fastapi import APIRouter

from backend.matrix.calculator import matrix_transpose, multiple_matrix_multiply, multiple_matrix_addition, matrix_det, \
    matrix_inverse, \
    matrix_adjoint, matrix_trace, matrix_power_n

router = APIRouter()


@router.post("/matrix_transpose/")
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


@router.post("/matrix_multiplication/")
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
            print("\n \n \n \n Final Result:", result)
            return {
                "result": result
            }
    return {"error": True, "message": "Invalid parameters."}


@router.post("/matrix_addition/")
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


@router.post("/matrix_determinant/")
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


@router.post("/matrix_inverse/")
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


@router.post("/matrix_adjoint/")
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


@router.post("/matrix_trace/")
async def matrix_trace_api(MatrixDict: dict):
    """ matrix_trace
        MatrixDict: {
            "matrix": [Nested Array]
        }
        """
    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if len(MatrixDict["matrix"]) != 0:
        result = matrix_trace(MatrixDict["matrix"])
        if result is not None:
            return {
                "result": result
            }
        return {"error": True, "message": "Not a Square Matrix. Trace cannot be found."}
    return {"error": True, "message": "Invalid matrix."}


@router.post("/matrix_power_n/")
async def matrix_power_n_api(MatrixDict: dict):
    """ matrix_trace
        MatrixDict: {
            "matrix": [Nested Array],
            "power": int
        }
        """

    if 'matrix' not in MatrixDict.keys():
        return {"error": True, "message": "Matrix not Defined."}

    if 'power' not in MatrixDict.keys():
        return {"error": True, "message": "Power not Defined."}

    if len(MatrixDict["matrix"]) != 0 and len(MatrixDict['power'] != 0):
        result, error = matrix_power_n(MatrixDict["matrix"], MatrixDict["power"])
        if result is not None:
            return {
                "result": result
            }
        return {"error": True, "message": error}
    return {"error": True, "message": "Invalid parameters."}

