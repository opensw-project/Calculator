def decimal_to_quaternary(decimal):
    quaternary = ''
    while decimal > 0:
        remainder = decimal % 4
        quaternary = str(remainder) + quaternary
        decimal //= 4
    return quaternary
