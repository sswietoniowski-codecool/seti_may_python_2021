def decimal_to_binary(decimal_number):
    digits = []
    while decimal_number > 0:
        digits.insert(0, decimal_number % 2)
        decimal_number = decimal_number // 2
    return digits


def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    number = 0
    for power, digit in enumerate(reversed(binary_digits)):
        number += digit * (2 ** power)
    return number


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    digits = []
    while decimal_number > 0:
        digits.insert(0, decimal_number % destination_base)
        decimal_number = decimal_number // destination_base
    return digits


def base_to_decimal(digits, original_base):
    number = 0
    for power, digit in enumerate(reversed(digits)):
        number += digit * (original_base ** power)
    return number


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    # 2 < base <= 16    
    if base > 16 or base < 2:
        raise ValueError(f'Wrong base! Input is bigger than 16. Your base: {base}')
    for digit in digits:
        if digit >= base:
            raise ValueError(f'Wrong digit! Your digit should be [0, {base - 1}]. Your digit: {digit}')
    alldigits = list('0123456789ABCDEF')
    string = ''
    for d in digits:
        string += alldigits[d]
    return string


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    number = base_to_decimal(original_digits, original_base)
    return decimal_to_base(number, destination_base)

