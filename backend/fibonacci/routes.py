from fastapi import APIRouter
from .calculator import n_th_fibonacci, calc_sum, is_fibonacci, is_fib_series, fib_series

router = APIRouter()


@router.post("/n_th_fibonacci/")
async def n_th_fibonacci_api(num: int):
    result = n_th_fibonacci(num)

    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": "Invalid input."}


@router.post("/calculate_sum/")
async def calc_sum_api(num: int):
    if num >= 0:
        return {
                "result": calc_sum(num)
            }
    return {"error": True, "message": "Invalid input."}


@router.post("/is_fibonacci_number/")
async def is_fibonacci_api(num: int):
    return {
        "message": "Number is Fibonacci.",
        "result": is_fibonacci(num)
    }


@router.post("/is_fibonacci_series/")
async def is_fib_series_api(list: list):
    result = is_fib_series(list)

    if result is not None:
        return {
            "message": "Series is Fibonacci.",
            "result": result
        }
    return {"error": True, "message": "Cannot be determined. At least 3 elements required."}


@router.post("/fibonacci_series/")
async def fib_series_api(num: int):
    result = fib_series(num)

    if result is not None:
        return {
            "result": result
        }
    return {"error": True, "message": "Invalid input."}