def decimal_to_binary(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    if not num_str.isnumeric():
        print("Not a decimal number.")
        return None, "Not a decimal number."

    num = int(num_str)
    if num < 2:
        print(f"Binary number of '{num}' : ", num)
        return num, None

    remainders = []
    q = num // 2
    r = num % 2
    remainders.append(r)

    while q >= 2:
        r = q % 2
        q = q // 2
        remainders.append(r)

    remainders.reverse()
    binary_str = f'{q}'
    for i in remainders:
        binary_str += str(i)

    binary_no = int(binary_str)

    print(f"Binary number of '{num}' : ", binary_no)
    return binary_no, None


def decimal_to_octal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    if not num_str.isnumeric():
        print("Not a decimal number.")
        return None, "Not a decimal number."

    num = int(num_str)
    if num < 8:
        print(f"Octal number of '{num}' : ", num)
        return num, None

    remainders = []
    q = num // 8
    r = num % 8
    remainders.append(r)

    while q >= 8:
        r = q % 8
        q = q // 8
        remainders.append(r)

    remainders.reverse()
    octal_str = f'{q}'
    for i in remainders:
        octal_str += str(i)

    octal_no = int(octal_str)

    print(f"Octal number of '{num}' : ", octal_no)
    return octal_no, None


def decimal_to_hexadecimal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    if not num_str.isnumeric():
        print("Not a decimal number.")
        return None, "Not a decimal number."

    num = int(num_str)
    if num < 10:
        print(f"Hexadecimal number of '{num}' : ", num)
        return num, None

    conversion_table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num < 16:
        hexadecimal_no = conversion_table[num]
        print(f"Hexadecimal number of '{num}' : ", hexadecimal_no)
        return hexadecimal_no, None

    remainders = []
    q = num // 16
    r = num % 16
    if 9 < r < 16:
        r = conversion_table[r]
    remainders.append(r)

    while q >= 16:
        r = q % 16
        q = q // 16

        if 9 < r < 16:
            r = conversion_table[r]

        remainders.append(r)

    remainders.reverse()
    hexadecimal_no = f'{q}'
    for i in remainders:
        hexadecimal_no += str(i)

    print(f"Hexadecimal number of '{num}' : ", hexadecimal_no)
    return hexadecimal_no, None


def binary_to_decimal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    possibilities = ['0', '1']
    for i in range(len(num_str)):
        if num_str[i] not in possibilities:
            print("Not a binary number.")
            return None, "Not a binary number."

    reversed_num_str = num_str[::-1]
    n = len(num_str)
    decimal_no = 0
    for i in range(n):
        decimal_no += int(reversed_num_str[i]) * (2 ** i)

    print(f"Decimal number of '{num_str}' : ", decimal_no)
    return decimal_no, None


def binary_to_octal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    possibilities = ['0', '1']
    for i in range(len(num_str)):
        if num_str[i] not in possibilities:
            print("Not a binary number.")
            return None, "Not a binary number."

    num = num_str
    n = len(num_str)
    while n % 3 != 0:
        num_str = str(0) + num_str
        n = len(num_str)

    pairs = n // 3

    num_str = num_str[::-1]
    dic = {}
    result = []
    for i in range(pairs):
        dic[i + 1] = num_str[3 * i: 3 * i + 3]
        n = n - 3

        value = int(dic[i + 1][0]) * 1 + int(dic[i + 1][1]) * 2 + int(dic[i + 1][2]) * 4
        result.append(value)

    result.reverse()
    octal_no = ''
    for i in result:
        octal_no += str(i)

    print(f"Octal number of '{num}' : ", octal_no)
    return octal_no, None


def binary_to_hexadecimal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    possibilities = ['0', '1']
    for i in range(len(num_str)):
        if num_str[i] not in possibilities:
            print("Not a binary number.")
            return None, "Not a binary number."

    num = num_str
    n = len(num_str)
    while n % 4 != 0:
        num_str = str(0) + num_str
        n = len(num_str)

    pairs = n // 4

    num_str = num_str[::-1]
    dic = {}
    result = []
    for i in range(pairs):
        dic[i + 1] = num_str[4 * i: 4 * i + 4]
        n = n - 4

        value = int(dic[i + 1][0]) * 1 + int(dic[i + 1][1]) * 2 + int(dic[i + 1][2]) * 4 + int(dic[i + 1][3]) * 8
        if 9 < value < 16:
            conversion_table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            value = conversion_table[value]
        result.append(value)

    result.reverse()
    hexadecimal_no = ''
    for i in result:
        hexadecimal_no += str(i)

    if hexadecimal_no.isnumeric():
        if 9 < int(hexadecimal_no) < 16:
            conversion_table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            hexadecimal_no = conversion_table[int(hexadecimal_no)]

    print(f"Hexadecimal number of '{num}' : ", hexadecimal_no)
    return hexadecimal_no, None


def octal_to_decimal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    possibilities = ['0', '1', '2', '3', '4', '5', '6', '7']
    for i in range(len(num_str)):
        if num_str[i] not in possibilities:
            print("Not an octal number.")
            return None, "Not an octal number."

    reversed_num_str = num_str[::-1]
    n = len(num_str)
    decimal_no = 0
    for i in range(n):
        decimal_no += int(reversed_num_str[i]) * (8 ** i)

    print(f"Decimal number of '{num_str}' : ", decimal_no)
    return decimal_no, None


def octal_to_binary(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    possibilities = ['0', '1', '2', '3', '4', '5', '6', '7']
    for i in range(len(num_str)):
        if num_str[i] not in possibilities:
            print("Not an octal number.")
            return None, "Not an octal number."

    result = ''
    n = len(num_str)

    for i in range(n):
        binary_no = decimal_to_binary(num_str[i])
        binary_str = str(binary_no)

        if len(binary_str) == 3:
            result = result + binary_str

        if len(binary_str) == 2:
            binary_str = '0' + binary_str
            result = result + binary_str

        if len(binary_str) == 1:
            binary_str = '00' + binary_str
            result = result + binary_str

    print(f"Binary number of '{num_str}' : ", result)
    return result, None


def octal_to_hexadecimal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    possibilities = ['0', '1', '2', '3', '4', '5', '6', '7']
    for i in range(len(num_str)):
        if num_str[i] not in possibilities:
            print("Not an octal number.")
            return None, "Not an octal number."

    result, error = octal_to_binary(num_str)
    binary_no = int(result)
    hexadecimal_no, error = binary_to_hexadecimal(str(binary_no))

    print(f"Hexadecimal number of '{num_str}' : ", hexadecimal_no)
    return hexadecimal_no, None


def hexadecimal_to_decimal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    for i in range(len(num_str)):
        possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        if num_str[i] not in possibilities:
            print("Not a hexadecimal number.")
            return None, "Not a hexadecimal number."

    if num_str.isnumeric():
        num = int(num_str)
        if num < 10:
            print(f"Decimal number of '{num}' : ", num)
            return num, None

    conversion_table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    for i in range(10, 16):
        if num_str == conversion_table[i]:
            print(f"Decimal number of '{num_str}' : ", i)
            return i, None

    reversed_num_str = num_str[::-1]
    n = len(num_str)
    decimal_no = 0
    for i in range(n):

        if reversed_num_str[i].isnumeric():
            decimal_no += int(reversed_num_str[i]) * (16 ** i)

        else:
            conversion_table_1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
            decimal_no += conversion_table_1[reversed_num_str[i]] * (16 ** i)

    print(f"Decimal number of '{num_str}' : ", decimal_no)
    return decimal_no, None


def hexadecimal_to_binary(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    for i in range(len(num_str)):
        possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        if num_str[i] not in possibilities:
            print("Invalid input. Not a hexadecimal number.")
            return None, "Not a hexadecimal number."

    result = ''
    n = len(num_str)

    for i in range(n):
        decimal_no, error = hexadecimal_to_decimal(num_str[i])
        binary_no = decimal_to_binary(decimal_no)
        binary_str = str(binary_no)

        if len(binary_str) == 4:
            result = result + binary_str

        if len(binary_str) == 3:
            binary_str = '0' + binary_str
            result = result + binary_str

        if len(binary_str) == 2:
            binary_str = '00' + binary_str
            result = result + binary_str

        if len(binary_str) == 1:
            binary_str = '000' + binary_str
            result = result + binary_str

    print(f"Binary number of '{num_str}' : ", result)
    return result, None


def hexadecimal_to_octal(num_str):
    if num_str[0] == '-':
        print("Not a positive value.")
        return None, "Not a positive value."

    for i in range(len(num_str)):
        possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        if num_str[i] not in possibilities:
            print("Invalid input. Not a hexadecimal number.")
            return None, "Not a hexadecimal number."

    result, error = hexadecimal_to_binary(num_str)
    binary_no = int(result)
    octal_no, error = binary_to_octal(str(binary_no))

    print(f"Hexadecimal number of '{num_str}' : ", octal_no)
    return octal_no, None


if __name__ == "__main__":
    number = input("Enter the decimal number : ")
    decimal_to_binary(number)

    print('\n')
    number = input("Enter the decimal number : ")
    decimal_to_octal(number)

    print('\n')
    number = input("Enter the decimal number : ")
    decimal_to_hexadecimal(number)

    print('\n')
    number = input("Enter the binary number : ")
    binary_to_decimal(number)

    print('\n')
    number = input("Enter the binary number : ")
    binary_to_octal(number)

    print('\n')
    number = input("Enter the binary number : ")
    binary_to_hexadecimal(number)

    print('\n')
    number = input("Enter the octal number : ")
    octal_to_binary(number)

    print('\n')
    number = input("Enter the octal number : ")
    octal_to_hexadecimal(number)

    print('\n')
    number = input("Enter the octal number : ")
    octal_to_decimal(number)

    print('\n')
    number = input("Enter the hexadecimal number : ")
    hexadecimal_to_decimal(number)

    print('\n')
    number = input("Enter the hexadecimal number : ")
    hexadecimal_to_binary(number)

    print('\n')
    number = input("Enter the hexadecimal number : ")
    hexadecimal_to_octal(number)
