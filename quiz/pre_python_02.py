""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""
a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
cal = input('어떤 연산을 하실 건가요? +,-,/,* 중 선택해주세요.: ')

if cal == "+":
    print('결과:{} '.format(a+b))
elif cal == "-":
    print('결과:{} '.format(a - b))
elif cal == "/":
    print('결과:{} '.format(a / b))
elif cal == "*":
    print('결과:{} '.format(a * b))
else:
    print('+,-,/,* 중 선택해주세요. ')
