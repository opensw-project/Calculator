def decimal_to_octal(decimal):
    octal = ''
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    return octal
 
