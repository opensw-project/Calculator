def in2post(infix):
    s = Stack()                                             # 스택 생성
    postfix = []                                            # 후위 표기법으로 바뀐 수식을 담아 줄 리스트
    for i in infix:
        if i == '(':                                        # 여는 괄호('(')일 경우 스택에 바로 push
            s.push(i)
        elif i == ')':                                      # 닫는 괄호(')')일 경우
            while s.top() != '(':                           # '('와 ')'사이의 연산자들을 모두 postfix 리스트에 추가
                postfix.append(s.pop())
            s.pop()                                         # 그리고 stack에 들어있던 '('는 삭제. (후위 표기법은 괄호를 표시하지 않으므로)
        elif i in priority:                                 # '+ - * /'일 경우
            while not s.isEmpty():                          # 스택이 비어 있지 않을 때
                if priority[s.top()] >= priority[i]:        # 스택의 top에 해당하는 연산자의 우선순위가 비교할 연산자의 우선순위보다 크거나 같을 경우
                    postfix.append(s.pop())                 # 해당 연산자(top)를 postfix 리스트에 추가한다
                else:
                    break
            s.push(i)                                       # 스택이 비어있을 경우엔 해당 연산자를 스택에 바로 push
        else:                                               # 피연산자(숫자)의 경우 리스트에 바로 추가
           postfix.append(i)
    while not s.isEmpty():                                  # '('보다 밑 스택에 남아있던 연산자들을
        postfix.append(s.pop())                             # 모두 리스트에 추가해준다

    return postfix                                          # 변환된 후위 표기식을 반환한다
