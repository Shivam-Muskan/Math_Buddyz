from sympy import symbols, Derivative, parse_expr, log


def f(n, exp):
    x = symbols('x')
    fx = exp.subs(x, n)

    return fx


def bisection(p, a, b, n, e):
    fa = f(a, p)
    fb = f(b, p)
    roots = {}

    total = float(log((b - a) / e) / log(2))
    print(total)

    if fa == 0:
        print(f"{a} is the root.")
        roots["Iteration 0"] = a
        return roots, total

    if fb == 0:
        print(f"{b} is the root.")
        roots["Iteration 0"] = b
        return roots, total

    if fa * fb > 0:
        print("No root lies between the given interval.")
        return None

    for i in range(n):
        fa = f(a, p)
        x = (a + b) / 2
        print(f"Root after iteration {i + 1} :", x)
        roots[f"Iteration {i + 1}"] = x
        fx = f(x, p)

        if fx == 0:
            print(f"{x} is the root for the given polynomial.")
            break

        else:
            if fa * fx < 0:
                b = x

            else:
                a = x

    return roots, total


def regula_falsi(p, a, b, n):
    fa = f(a, p)
    fb = f(b, p)
    roots = {}

    if fa == 0:
        print(f"{a} is the root.")
        roots["Iteration 0"] = a
        return roots

    if fb == 0:
        print(f"{b} is the root.")
        roots["Iteration 0"] = b
        return roots

    if fa * fb > 0:
        print("No root lies between the given interval.")
        return None

    for i in range(n):
        fa = f(a, p)
        fb = f(b, p)
        x = (a * fb - b * fa) / (fb - fa)
        print(f"Root after iteration {i + 1} :", float(x))
        roots[f"Iteration {i + 1}"] = float(x)
        fx = f(x, p)

        if fx == 0:
            print(f"{x} is the root for the given polynomial.")
            break

        else:
            if fa * fx < 0:
                b = x

            else:
                a = x

    return roots


def newton_raphson(p, x0, n):
    fx = f(x0, p)
    roots = {}

    if fx == 0:
        print(f"{x0} is the root of the equation.")
        roots["Iteration 0"] = x0
        return roots

    for i in range(n):
        fx = f(x0, p)
        x = symbols('x')
        g = Derivative(p, x).doit()
        gx = float(f(x0, g))
        if gx == 0:
            print("Error! This method is not applicable when f'(x) = 0")
            x = None
            break

        else:
            x = x0 - fx / gx
            print(f"Root after iteration {i + 1} :", x)
            roots[f"Iteration {i + 1}"] = x
            x0 = x

    return roots


def secant(p, a, b, n):
    fa = f(a, p)
    fb = f(b, p)

    if fa == fb:
        print("Error! This method is not applicable here as f(a) = f(b).")
        return None

    roots = {}
    for i in range(n):
        x = b - ((a - b) / (fa - fb)) * fb
        print(f"Root after iteration {i + 1} :", x)
        roots[f"Iteration {i + 1}"] = x
        a = b
        b = x
        fa = f(a, p)
        fb = f(b, p)

    return roots


def fixed_point_iteration(p, x0, n):
    x = symbols('x')
    g = Derivative(p, x).doit()
    gx = float(f(x0, g))
    roots = {}

    for i in range(n):
        if abs(gx) < 1:
            x = f(x0, p)
            print(f"Root after iteration {i + 1} :", float(x))
            roots[f"Iteration {i + 1}"] = float(x)
            x0 = x

        else:
            print("Condition |g'(x0)| < 1 fails.")
            return None

    return roots


if __name__ == '__main__':
    expr = parse_expr(input("Enter the polynomial in x, f(x)= "))
    a = float(input("Enter the lower limit of the interval, i.e., a = "))
    b = float(input("Enter the upper limit of the interval, i.e., b = "))
    num = int(input("Enter the number of iterations:"))
    e = float(input("Tolerance error:"))

    print("\nBisection Method :")
    print(bisection(expr, a, b, num, e))

    print("\nregula_falsi Method :")
    print(regula_falsi(expr, a, b, num))

    print("\nnewton_raphson Method :")
    x0 = float(input("Enter num, x0 = "))
    print(newton_raphson(expr, x0, num))

    print("\nsecant Method :")
    print(secant(expr, a, b, num))

    print("\nfixed_point_iteration Method :")
    exp1 = parse_expr(input("Enter the polynomial in x, g(x) such that x = g(x) from the given equation :"))
    x0 = float(input("Enter x0 such that  |g’(x)| < 1 :"))
    print(fixed_point_iteration(exp1, x0, num))
