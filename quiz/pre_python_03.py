"""
3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요

예시
<입력>
첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력
두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력

<출력>
첫 번째(두 번째) 참가자의 승리입니다. or 비겼습니다.
"""
import random

first_num = [1,2,3,4,5,6]
second_num = [1,2,3,4,5,6]

input("첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ")
random.shuffle(first_num)
first_result = random.choice(first_num)
print(first_result)

input("두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ")
random.shuffle(second_num)
second_result = random.choice(second_num)
print(second_result)

if first_result == second_result:
    print("비겼습니다.")
elif first_result > second_result:
    print("첫 번째 참가자의 승리입니다.")
else:
    print("두 번째 참가자의 승리입니다.")