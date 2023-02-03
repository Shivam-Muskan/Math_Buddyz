from fastapi import APIRouter

from .calculator import decimal_to_binary, decimal_to_octal, decimal_to_hexadecimal, binary_to_decimal, binary_to_octal, \
    binary_to_hexadecimal

router = APIRouter()


@router.post("/decimal_to_binary/")
async def decimal_to_binary_api(num: int):
    """ decimal_to_binary
    :param num: int
    """
    result = decimal_to_binary(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": "Invalid input."}


@router.post("/decimal_to_octal/")
async def decimal_to_octal_api(num: int):
    """ decimal_to_octal
    :param num: int
    """
    result = decimal_to_octal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": "Invalid input."}


@router.post("/decimal_to_hexadecimal/")
async def decimal_to_hexadecimal_api(num: int):
    """ decimal_to_hexadecimal
    :param num: int
    """
    result = decimal_to_hexadecimal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": "Invalid input."}


@router.post("/binary_to_decimal/")
async def binary_to_decimal_api(num: str):
    """ binary_to_decimal
    :param num: str
    """

    result, error = binary_to_decimal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/binary_to_octal/")
async def binary_to_octal_api(num: str):
    """ binary_to_octal
    :param num: str
    """

    result, error = binary_to_octal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/binary_to_hexadecimal/")
async def binary_to_hexadecimal_api(num: str):
    """ binary_to_hexadecimal
    :param num: str
    """

    result, error = binary_to_hexadecimal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}
