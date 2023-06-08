import tkinter as tk

disValue = 0
operator = {'+':1, '-':2, '/':3, '*':4, 'C':5, '=':6}
stoValue = 0
opPre = 0

### 0~9까지의 숫자를 클릭했을때
def number_click(value):
    # print('숫자 ',value)
    global disValue
    
    disValue = (disValue*10) + value #숫자를 클릭할때마다 10의 자리씩 이동한다.
    str_value.set(disValue)          #화면에 숫자를 나타낸다.
    
### C를 클릭하여 clear할때
def clear():
    global disValue, stoValue, opPre
    #주요 변수 초기화
    stoValue = 0
    opPre = 0
    disValue = 0
    str_value.set(str(disValue)) #화면을 지운다.

### + ~ = 연산자를 클릭했을때
def oprator_click(value):
    # print('명령 ', value)
    global disValue, operator, stoValue, opPre
    
    #value의 값에 따라 숫자로 연산자를 변경한다.(+는 1로, -는 2로..)
    op = operator[value] 
    
    if op == 5:              # C (clear)
        clear()
    elif disValue == 0:      #현재 화면에 출력된 값이 0일때
        opPre = 0
    elif opPre == 0:         #연산자가 한번도 클릭되지 않았을때
        opPre = op           #현재 눌린 연산자가 있으면 저장
        stoValue = disValue  #현재까지의 숫자를 저장
        disValue = 0         #연산자 이후의 숫자를 받기 위해 초기화
        str_value.set(str(disValue)) #0으로 다음 숫자를 받을 준비
    elif op == 6:             #'=  결과를 계산하고 출력한다.
        if opPre == 1: # +
            disValue = stoValue + disValue
        if opPre == 2: # -
            disValue = stoValue - disValue
        if opPre == 3: # /
            disValue = stoValue / disValue
        if opPre == 4: # *
            disValue = stoValue * disValue
        
        str_value.set(str(disValue)) #최종 결과 값을 출력한다.
        disValue = 0
        stoValue = 0
        opPre = 0
    else:
        clear()

def button_click(value):
    # print(value)
    try:
        value = int(value)      #정수로 변환한다.
        
        #정수가 아닌 경우 except가 발생하여 아래 except로 이동한다.
        number_click(value)     #정수인 경우 number_click( )를 호출
    except:
        oprator_click(value)    #정수가 아닌 연산자인 경우 여기로!!
        
win = tk.Tk()
win.title('계산시')

str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable=str_value, justify='right', bg = 'white',fg='red')
dis.grid(column=0, row=0, columnspan=4, ipadx=80, ipady=30)

calItem = [['1','2','3','4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

for i,items in enumerate(calItem):
    for k,item in enumerate(items):
        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'
        bt = tk.Button(win, 
            text=item, 
            width=10, 
            height=5,
            bg=color,
            fg = 'white',
            command = lambda cmd=item: button_click(cmd)
            )
        bt.grid(column=k, row=(i+1))

win.mainloop()
