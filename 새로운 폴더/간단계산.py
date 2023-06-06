while True:
    a=float(input('n1:'))
    b=float(input('n2:'))

    if a==b==0:
        print('종료합니다.')
    c=input('연산자:')
    if c=='*':
        d=a*b
        print('계산값은', d, '입니다.')
        continue
    if c=='+':
        d=a+b
        print('계산값은', d, '입니다.')
        continue
    if c=='-':
        d=a-b
        print('계산값은', d, '입니다.')
        continue
    if c=='/':
        d=a/b
        print('계산값은', d, '입니다.')
        continue 

    if c!='+' or c!='-' or c!='*' or c!='/': 
        while True:
            print('연산자를 다시 입력하세요.')
            c=input('연산자:')

            if c=='*':
                d=a*b
                print('계산값은', d, '입니다.')
                break
            if c=='+':
                d=a+b
                print('계산값은', d, '입니다.')
                break
            if c=='-':
                d=a-b
                print('계산값은', d, '입니다.')
                break
            if c=='/':
                d=a/b
                print('계산값은', d, '입니다.')
                break
