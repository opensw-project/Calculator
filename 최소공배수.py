from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def get_lcm(numbers):
    lcm_value = numbers[0]  
    for number in numbers[1:]:
        lcm_value = lcm(lcm_value, number)
    return lcm_value

numbers = []
num = int(input('숫자를 입력'))
numbers.append(num)

print(get_lcm(numbers))
