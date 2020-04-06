""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""

def calculator():
    x = input("첫 번째 수를 입력하세요 : ")
    y = input("두 번째 수를 입력하세요 : ")
    z = input("어떤 연산을 하실 건가요? : ")

    if z == '+':
        result = int(x) + int(y)
    elif z == '-':
        result = int(x) - int(y)
    elif z == '*':
        result = int(x) * int(y)
    else:
        if int(y) == 0:
            print(">>> 0으로 나눌 수 없습니다. <<<")
            return
        else:
            result = int(x) / int(y)

    print(result)

calculator()