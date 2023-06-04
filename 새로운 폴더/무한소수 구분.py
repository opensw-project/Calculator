from decimal import Decimal

def is_infinite_decimal(num):
    try:
        Decimal(num)
    except:
        return False
    return True
