""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""

# import operator
#
# ops = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
# }
# x = int(input("첫 번째 수를 입력하세요 : "))
# y = int(input("두 번째 수를 입력하세요 : "))
# z = input("어떤 연산을 하실 건가요? : ")
#
# ops_D = ops[z]
# result = ops_D(x, y)
# print(result)
# import 모듈 확인하기

# 변수명 만드는거 너무 어렵다.. 그런데 이렇게하면 기본 연산자 밖에 못쓰는데...

fir = int(input("첫 번째 수를 입력하세요 : "))
sec = int(input("두 번째 수를 입력하세요 : "))
op = input("어떤 연산을 하실 건가요? : ")

if op == "+":
    print(fir + sec)
elif op == "-":
    print(fir - sec)
elif op == "*":
    print(fir * sec)
elif op == "/":
    print(fir / sec)
elif op == "**":
    print(fir ** sec)
else:
    print("오류입니다, 다시 작동해주세요. ")

# 다른 연산자 찾아보기, if 문을 썼을때 효율적인가? 피드백 받기