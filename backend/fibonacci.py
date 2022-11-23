import math


# Function for nth fibonacci number :
def n_th_fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return n_th_fibonacci(n - 1) + n_th_fibonacci(n - 2)


# sum of Fibonacci Numbers
def calc_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + n_th_fibonacci(i)

    return sum


# Check if number is fibonacci or not
def is_fibonacci(n):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    result = is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
    if result:
        print(n, " is a fibonacci number.")
    else:
        print(n, " is not a fibonacci number.")


num1 = int(input("Input the number : "))
result1 = n_th_fibonacci(num1)
print("The nth fibonnaci number = ", result1)

num2 = int(input("Input the number to find the sum  : "))
result2 = calc_sum(num2)
print(f"The Sum of {num2} fibonnaci numbers = ", result2)

num3 = int(input("Input the number to check whether its fibonacci or not : "))
is_fibonacci(num3)
