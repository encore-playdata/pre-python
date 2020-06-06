""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""
def sum (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b

a = int(input("첫 번째 수를 입력하세요 :"))
b = int(input("두 번째 수를 입력하세요 :"))
z = input("어떤 연산을 하실 건가요? :")

if z == '+':
    print (sum(a,b))
elif z == '-':
    print(sub(a,b))
elif z == '*':
    print(mul(a,b))
elif z == '/':
    print(div(a,b))
elif z == '%':
    print(rem(a,b))
else:
    print("잘못된 선택입니다.")

