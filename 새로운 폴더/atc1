n = int(input())
t_pre = 0
x_pre = 0
y_pre = 0
flag = True
for _ in range(n):
    t,x,y = map(int,input().split())
    d = abs(x-x_pre)+abs(y-y_pre)
    time = t-t_pre
    t_pre = t
    x_pre = x
    y_pre = y
    if time<d or time%2!=d%2:
        flag=False
print("Yes" if flag else "No")

#https://tysonblog-whitelabel.com/atcoder-beginners-selection_practice11 解説リンク
