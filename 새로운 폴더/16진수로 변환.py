def decimal_to_hexadecimal(decimal):
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder + 55) + hexadecimal
        decimal //= 16
    return hexadecimal
