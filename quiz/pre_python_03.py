"""
3.
Enter key 를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요.

예시
<입력>
첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력
두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력

<출력>
첫 번째(두 번째) 참가자의 승리입니다. or 비겼습니다.
"""

import random  # random 라이브러리 사용

first_num = random.randrange(1, 7)      # randrange(a, b) 랜덤한 정수 반환
input("첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ")     # Enter key 입력
print("%d" % first_num)     # 1 이상 7 미만의 난수 출력
second_num = random.randrange(1, 7)     # randrange(a, b) b를 포함하지 않는다
input("두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ")     # Enter key 입력
print("%d" % second_num)    # 1 이상 7 미만의 난수 출력

if first_num > second_num:      # first_num 가 second_num 보다 크다면
    print("첫 번째 참가자의 승리입니다.")
elif first_num < second_num:    # first_num 가 second_num 보다 작다면
    print("두 번째 참가자의 승리입니다.")
else:
    print("비겼습니다.")     # 둘 다 아니라면
