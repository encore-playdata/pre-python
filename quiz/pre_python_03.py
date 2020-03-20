"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요


예시
<입력>
첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력
두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력

<출력>
첫 번째(두 번째) 참가자의 승리입니다. or 비겼습니다.

"""
import random

# def first_participant():
#     return random.randint(1, 6)
#
# def second_participant():
#     return random.randint(1, 6)
# 어짜피 하나의 값인데 함수가 왜 필요해.. 함수는 언제 써야하지??

first = random.randint(1, 6)
second = random.randint(1, 6)

input("첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ")
print(first)
input("두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ")
print(second)


if first > second:
    print("첫 번째 참가자의 승리입니다.")
elif first < second:
    print("두 번째 참가자의 승리입니다.")
else:
    print("비겼습니다.")

# 이것도 너무 코드가 긴데.. 디렉토리를 이용하면 쉬울 것 같음 그리고 input 바로 옆에 값을 넣고 싶은데..