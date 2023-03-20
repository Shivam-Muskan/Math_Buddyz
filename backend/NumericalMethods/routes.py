from fastapi import APIRouter, Query
from sympy import parse_expr

from backend.NumericalMethods.calculator import bisection, regula_falsi, newton_raphson, secant, fixed_point_iteration

router = APIRouter()


@router.post("/bisection_method/")
async def bisection_api(p: str = Query(default="x**3-5*x-9", description="Enter the polynomial in x"),
                        a: float = Query(default=2, description="Enter the lower limit of the interval"),
                        b: float = Query(default=3, description="Enter the upper limit of the interval"),
                        n: int = Query(default=0, description="Enter the number of iterations")):
    p = parse_expr(p)
    result, message = bisection(p, a, b, n)

    if result is not None:
        return {
            "roots": result,
            "message": message
        }

    return {"error": True, "message": message}


@router.post("/regula_falsi/")
async def regula_falsi_api(p: str = Query("x**3-5*x-9", description="Enter the polynomial in x"),
                           a: float = Query(2, description="Enter the lower limit of the interval"),
                           b: float = Query(3, description="Enter the upper limit of the interval"),
                           n: int = Query(0, description="Enter the number of iterations")):
    p = parse_expr(p)
    result, message = regula_falsi(p, a, b, n)
    if result is not None:
        return {
            "roots": result,
            "message": message
        }

    return {"error": True, "message": message}


@router.post("/newton_raphson/")
async def newton_raphson_api(p: str = Query("x**3-5*x-9", description="Enter the polynomial in x"),
                             x0: float = Query(2, description="Enter the value of x0"),
                             n: int = Query(0, description="Enter the number of iterations")):
    p = parse_expr(p)
    result, message = newton_raphson(p, x0, n)
    if result is not None:
        return {
            "roots": result,
            "message": message
        }

    return {"error": True, "message": message}


@router.post("/secant/")
async def secant_api(p: str = Query("x**3-5*x-9", description="Enter the polynomial in x"),
                     a: float = Query(2, description="Enter the lower limit of the interval"),
                     b: float = Query(3, description="Enter the upper limit of the interval"),
                     n: int = Query(0, description="Enter the number of iterations")):
    p = parse_expr(p)
    result, message = secant(p, a, b, n)
    if result is not None:
        return {
            "roots": result,
            "message": message
        }

    return {"error": True, "message": message}


@router.post("/fixed_point_iteration/")
async def fixed_point_iteration_api(
        p: str = Query("cbrt((2*x + 5)/2)", description="Enter the polynomial in x, g(x) such that x = "
                                                        "g(x) from the given equation"),
        x0: float = Query(1.5, description="Enter x0 such that  |g’(x0)| < 1"),
        n: int = Query(0, description="Enter the number of iterations")):

    p = parse_expr(p)
    result, message = fixed_point_iteration(p, x0, n)
    if result is not None:
        return {
            "roots": result,
            "message": message
        }

    return {"error": True, "message": message}
