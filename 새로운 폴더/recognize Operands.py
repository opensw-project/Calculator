def recognize_Operands(infix):
    numbers = list('0123456789.')                       # 실수 계산기 이므로, 모든 피연산자는 0~9인 정수와 .으로 이루어진다
    recognized = []                                      # 수식의 숫자들을 피연산자로 인식하여 다시 담아 줄 리스트

    i = 0
    while i < len(infix):
        j = 1
        if infix[i] in numbers:                         # 연산자가 아닐 경우, 즉 숫자 또는 .일 경우
            while i + j < len(infix):                   # 해당 요소의 다음 요소도 숫자 또는 .인지를 판별하고
                if infix[i + j] in numbers:
                    j += 1
                else:
                    break
            recognized.append(''.join(infix[i:i + j]))   # 이들을 하나로, 즉 하나의 숫자로 인식 할 수 있도록 묶어준다
            i += j
        else:                                           # 연산자일 경우엔 리스트에 바로 추가해준다
            recognized.append(infix[i])
            i += 1
    return recognized
