def calculate(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            else:
                print("지원하지 않는 연산자입니다.")
                return None

            stack.append(result)

    if len(stack) == 1:
        return stack[0]
    else:
        print("잘못된 식입니다.")
        return None

# 계산식 입력
expression = input("계산식을 입력하세요: ").split()

# 계산 수행
result = calculate(expression)
print("계산 결과:", result) 
 
