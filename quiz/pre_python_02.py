""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""
def calculator(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    else:
        return first_number / second_number

first_number = int(input("첫 번째 수를 입력하세요 : "))
second_number = int(input("두 번째 수를 입력하세요 : "))
operator = input("어떤 연산을 하실 건가요? : ")
while operator not in ['+', '-', '*', '/']:
    print("연산기호가 잘못 입력되었습니다.")
    operator = input("어떤 연산을 하실 건가요? : ")

print(calculator(first_number, second_number, operator))
