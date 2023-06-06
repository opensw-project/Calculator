n = int(input())

t,f = 0, 0

for i in range(n):
    a = int(input())
    if a == 1:
        t += 1

    else:
        f += 1

if t> f:
    print('aa')

else:
    print('bb')
