""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""
def calculator(a,b,c):
    if c == '*':
        print(a*b)
    elif c =='/':
        if b == 0:
            print('0으로 나눌 수 없습니다.')
            b= int(input('두 번째 수를 입력하세요.:'))
            calculator(a,b,c)
            print(a/b)
        else:
            print(a / b)
    elif c =='+':
        print(a+b)
    elif c =='-':
        print(a-b)
    else:
        print('연산기호를 잘 못 입력 하셨습니다.')
        c = input('어떤 연산을 하실 건가요? :')
        calculator(a,b,c)

a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
c = input('어떤 연산을 하실 건가요? : ')

calculator(a,b,c)

