def decimal_to_binary(num):
    if num < 0:
        print("Not a Positive value.")
        return None

    if num < 2:
        print(f"Binary number of {num} : ", num)
        return num

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

    print(f"Binary number of {num} : ",binary_no)
    return binary_no


def decimal_to_octal(num):
    if num < 0:
        print("Not a Positive value.")
        return None

    if num < 8:
        print(f"Octal number of {num} : ", num)
        return num

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

    print(f"Octal number of {num} : ", octal_no)
    return octal_no


def decimal_to_hexadecimal(num):
    if num < 0:
        print("Not a Positive value.")
        return None

    if num < 10:
        print(f"Hexadecimal number of {num} : ", num)
        return num

    conversion_table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num < 16:
        hexadecimal_no = conversion_table[num]
        print(f"Hexadecimal number of {num} : ", hexadecimal_no)
        return hexadecimal_no

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

    print(f"Hexadecimal number of {num} : ", hexadecimal_no)
    return hexadecimal_no


if __name__ == "__main__":
    number = int(input("Enter the number : "))
    decimal_to_binary(number)

    print('\n')
    number = int(input("Enter the number : "))
    decimal_to_octal(number)

    print('\n')
    number = int(input("Enter the number : "))
    decimal_to_hexadecimal(number)

