from math import sqrt


# Function for nth fibonacci number
def n_th_fibonacci(n):
    if n <= 0:
        print("Incorrect input")
        return None

    # if n == 1:
    #     return 0
    #
    # if n == 2:
    #     return 1

    # return n_th_fibonacci(n - 1) + n_th_fibonacci(n - 2)
    res = (((1 + sqrt(5)) ** n) - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))
    return res


# Find Fibonacci Series of a number
def fib_series(n):
    series = []
    if n <= 0:
        print("Incorrect input")
        return None

    if n == 1:
        series.append(0)
        return series

    if n == 2:
        series.append(0)
        series.append(1)
        return series

    series.append(0)
    series.append(1)
    for n in range(3, n + 1):
        num = n_th_fibonacci(n - 1) + n_th_fibonacci(n - 2)
        series.append(num)
    return series


# sum of Fibonacci Numbers
def calc_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + n_th_fibonacci(i)

    return sum


# Check if number is fibonacci or not
def is_perfect_square(x):
    s = int(sqrt(x))
    return s * s == x


def is_fibonacci(n):
    if n >= 0:
        result = is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
        if result:
            print(n, " is a fibonacci number.", '\n')
            return result
        print(n, " is not a fibonacci number.", '\n')
        return result

    print(n, " is not a fibonacci number.", '\n')
    return False


# Check if given list of numbers represents Fibonacci series
def is_fib_series(l):
    flag = 0
    if len(l) > 2:
        for i in range(2, len(l)):
            if l[i] == l[i - 1] + l[i - 2]:
                continue

            print("The series is not fibonacci.")
            flag = 1
            break

        if flag == 0:
            print("The series is fibonacci.")
            return True
        return False

    print("Cannot be determined. At least 3 elements required.", '\n')
    # li = [int(item) for item in input("Enter the list items : ").split(',')]
    # is_fib_series(li)
    return None


if __name__ == "__main__":
    num1 = int(input("Input the number : "))
    result1 = n_th_fibonacci(num1)
    print("The nth fibonnaci number = ", result1, '\n')

    num2 = int(input("Input the number to find the sum  : "))
    result2 = calc_sum(num2)
    print(f"The Sum of {num2} fibonnaci numbers = ", result2, '\n')

    num3 = int(input("Input the number to check whether its fibonacci or not : "))
    is_fibonacci(num3)

    num4 = int(input("Input the number to find the series  : "))
    result3 = fib_series(num4)
    print(f"The Series of {num4} fibonacci numbers = ", result3, '\n')

    list1 = [int(item) for item in input("Enter the list items : ").split(',')]
    is_fib_series(list1)
