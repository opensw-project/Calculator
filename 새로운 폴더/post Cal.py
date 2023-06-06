def post_Cal(postfix):
    s = Stack()

    for i in postfix:
        if i in priority:                                   # 연산자일 경우
            num1 = s.pop()                                  # 스택에 쌓여 있던 두 피연산자(숫자)를 꺼내
            num2 = s.pop()
            if i == '+':                                    # 덧셈(+)
                s.push(num2 + num1)
            elif i == '-':                                  # 뺄셈(-)
                s.push(num2 - num1)
            elif i == '/':                                  # 나눗셈(/)
                s.push(num2 / num1)
            elif i == '*':                                  # 곱셈(*)
                s.push(num2 * num1)                         # 두 피연산자에 대해 각 연산자에 해당하는 연산을 수행한 값을 스택에 push해준다

        else:                                               # 숫자일 경우
            s.push(float(i))                                # 해당 숫자를 float 자료형으로 스택에 push(실수 계산기이므로)

    return s.pop()                                          # 계산된 값을 반환한다
