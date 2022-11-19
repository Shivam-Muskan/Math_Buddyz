'''

Addition
Subtraction
Multiplication
Division
Powers & Roots
Multiple Operations

'''
import ast
import re
from numbers import Number
from typing import List
from asteval import Interpreter

number = 1 + 2 - 3 * 4
safe_eval = Interpreter()
user_input = input("1+2-3*4/9: ")
number_input = safe_eval.eval(user_input)
print(number_input)

