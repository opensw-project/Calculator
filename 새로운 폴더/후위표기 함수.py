def search_Error(expr):
    possible = list('0123456789.()+-*/')            # 수식에 입력 가능한 문자들의 리스트
    integers = list('0123456789')                   # 0~9까지의 정수들의 리스트
    operators = list('+-*/')                        # 수식에 사용될 연산자들의 리스트
    s = Stack()

    for i in range(len(expr)):
        if expr[i] not in possible:                 # 입력 가능한 문자가 아닐 경우 해당 위치 반환
            return i
        elif i == 0 and expr[i] in operators:       # 연산자가 수식의 가장 앞에 위치할 경우 해당 위치 반환 (ex. *123+4...)
            return i
        elif expr[i] in operators:
            if i + 1 == len(expr):                  # 연산자 뒤에 피연산자가 오지 않고 수식이 끝날 경우 위치 반환 (ex. 1+2+)
                return i
            else:                                   # 연속해서 연산자가 위치할 경우 해당 위치 반환 (ex. 1+*2...)
                if expr[i + 1] in operators:
                    return i + 1
        elif expr[i] == '(':                        # 수식에서 '('가 발견되었을 때
            if expr[i - 1] in integers and i != 0:  # 여는 괄호('(') 앞에 정수가 올 경우 해당 위치 반환
                return i
            else:
                if s.isEmpty():                     # 스택에 이미 값이 들어있으면 해당 위치 반환
                    s.push('(')                     # 스택이 비어있으면 push
                else:
                    return i
        elif expr[i] == ')':                        # 수식에서 ')'가 발견되었을 때
            if s.isEmpty():                         # 스택이 비어있으면
                return i                            # 해당 위치 반환
            elif expr[i + 1] in integers and i != len(expr) - 1:
                return i + 1                        # 닫는 괄호(')') 뒤에 정수가 올 경우 해당 위치 반환
            else:
                s.push(')')                         # 스택이 비어있지 않다면 해당 값을 스택에 push

    if not s.isEmpty():                             # 수식에 '('는 존재 하지만 ')'는 존재하지 않는 경우
        if s.pop() == '(':
            return len(expr)                        # 수식의 마지막 위치를 반환
