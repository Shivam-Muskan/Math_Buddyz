from fastapi import APIRouter

from .calculator import decimal_to_binary, decimal_to_octal, decimal_to_hexadecimal, binary_to_decimal, binary_to_octal, \
    binary_to_hexadecimal, octal_to_decimal, octal_to_binary, octal_to_hexadecimal, hexadecimal_to_decimal,  hexadecimal_to_binary, hexadecimal_to_octal

router = APIRouter()


@router.post("/decimal_to_binary/")
async def decimal_to_binary_api(num: int):
    """ decimal_to_binary
    :param num: int
    """
    result, error = decimal_to_binary(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/decimal_to_octal/")
async def decimal_to_octal_api(num: int):
    """ decimal_to_octal
    :param num: int
    """
    result, error = decimal_to_octal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/decimal_to_hexadecimal/")
async def decimal_to_hexadecimal_api(num: int):
    """ decimal_to_hexadecimal
    :param num: int
    """
    result, error = decimal_to_hexadecimal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


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


@router.post("/octal_to_decimal/")
async def octal_to_decimal_api(num: str):
    """ octal_to_decimal
    :param num: str
    """

    result, error = octal_to_decimal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/octal_to_binary/")
async def octal_to_binary_api(num: str):
    """ octal_to_binary
    :param num: str
    """

    result, error = octal_to_binary(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/octal_to_hexadecimal/")
async def octal_to_hexadecimal_api(num: str):
    """ octal_to_hexadecimal
    :param num: str
    """

    result, error = octal_to_hexadecimal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/hexadecimal_to_decimal/")
async def hexadecimal_to_decimal_api(num: str):
    """ hexadecimal_to_decimal
    :param num: str
    """

    result, error = hexadecimal_to_decimal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/hexadecimal_to_binary/")
async def hexadecimal_to_binary_api(num: str):
    """ hexadecimal_to_binary
    :param num: str
    """

    result, error = hexadecimal_to_binary(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}


@router.post("/hexadecimal_to_octal/")
async def hexadecimal_to_octal_api(num: str):
    """ hexadecimal_to_octal
    :param num: str
    """

    result, error = hexadecimal_to_octal(num)
    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": error}