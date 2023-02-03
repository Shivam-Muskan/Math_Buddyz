from fastapi import APIRouter, Query
from sympy import parse_expr

from backend.NumericalMethods.calculator import bisection, regula_falsi, newton_raphson, secant, fixed_point_iteration

router = APIRouter()


@router.post("/bisection_method/")
async def bisection_api(p: str = Query(None, description="Enter the polynomial in x"),
                        a: float = Query(None, description="Enter the lower limit of the interval"),
                        b: float = Query(None, description="Enter the upper limit of the interval"),
                        n: int = Query(None, description="Enter the number of iterations"),
                        err: float = Query(None, description="Enter the tolerance error to find the minimum no of "
                                                             "iterations required. ")):
    p = parse_expr(p)
    result, total = bisection(p, a, b, n, err)
    if result is not None:
        return {
            "Roots of the given equation": result,
            "Min number of iterations required >= ": total
        }

    return {"error": True, "message": "Cannot be determined."}


@router.post("/regula_falsi/")
async def regula_falsi_api(p: str = Query(None, description="Enter the polynomial in x"),
                        a: float = Query(None, description="Enter the lower limit of the interval"),
                        b: float = Query(None, description="Enter the upper limit of the interval"),
                        n: int = Query(None, description="Enter the number of iterations")):
    p = parse_expr(p)
    result = regula_falsi(p, a, b, n)
    if result is not None:
        return {
            "message": "Roots of the given equation:",
            "result": result
        }

    return {"error": True, "message": "Cannot be determined."}


@router.post("/newton_raphson/")
async def newton_raphson_api(p: str = Query(None, description="Enter the polynomial in x"),
                             x0: float = Query(None, description="Enter the value of x0"),
                             n: int = Query(None, description="Enter the number of iterations")):
    p = parse_expr(p)
    result = newton_raphson(p, x0, n)
    if result is not None:
        return {
            "message": "Roots of the given equation:",
            "result": result
        }

    return {"error": True, "message": "Cannot be determined."}


@router.post("/secant/")
async def secant_api(p: str = Query(None, description="Enter the polynomial in x"),
                     a: float = Query(None, description="Enter the lower limit of the interval"),
                     b: float = Query(None, description="Enter the upper limit of the interval"),
                     n: int = Query(None, description="Enter the number of iterations")):
    p = parse_expr(p)
    result = secant(p, a, b, n)
    if result is not None:
        return {
            "message": "Roots of the given equation:",
            "result": result
        }

    return {"error": True, "message": "Cannot be determined."}


@router.post("/fixed_point_iteration/")
async def fixed_point_iteration_api(p: str = Query(None, description="Enter the polynomial in x, g(x) such that x = "
                                                                     "g(x) from the given equation"),
                                    x0: float = Query(None, description="Enter x0 such that  |g’(x)| < 1"),
                                    n: int = Query(None, description="Enter the number of iterations")):
    p = parse_expr(p)
    result = fixed_point_iteration(p, x0, n)
    if result is not None:
        return {
            "message": "Roots of the given equation:",
            "result": result
        }

    return {"error": True, "message": "Cannot be determined."}
