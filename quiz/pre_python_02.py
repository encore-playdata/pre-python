""""
2.
if 문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오.

예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""

first_num = int(input("첫 번째 수를 입력하세요 : "))      # 첫 번째 수 입력란
second_num = int(input("두 번째 수를 입력하세요 : "))     # 두 번째 수 입력란
calculate = input("어떤 연산을 하실 건가요? : ")          # 연산자 입력란


if calculate == "+":    # +가 입력된다면
    print(first_num + second_num)   # 첫 번째 수와 두 번째 수를 더한 수
elif calculate == "-":  # -가 입력된다면
    print(first_num - second_num)   # 첫 번째 수와 두 번째 수를 뺀 수
elif calculate == "*":  # *가 입력된다면
    print(first_num * second_num)   # 첫 번째 수와 두 번째 수를 곱한 수
elif calculate == "/":  # /가 입력된다면
    print(first_num / second_num)   # 첫 번째 수와 두 번째 수를 나눈 수

