"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요


예시
<입력>
첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력
두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력

<출력>
첫 번째(두 번째) 참가자의 승리입니다. or 비겼습니다.

"""

# 내가 작성한 답안
import random
p1 = random.randrange(1,7)
print("첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : %d" % p1)
p2 = random.randrange(1,7)
print("두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : %d" % p2)

if p1 > p2:
    print("첫 번째 참가자의 승리입니다")
elif p1 < p2:
    print("두 번째 참가자의 승리입니다")
else:
    print("비겼습니다")

# 실제 답안
import random
input("첫 번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ")
p1 = random.randrange(1,7)
print("첫 번째 참가자 : %d입니다." % p1)
p2 = random.randrange(1,7)
print("두 번째 참가자 : %d입니다." % p2)

if p1 > p2:
    print("첫 번째 참가자의 승리입니다")
elif p1 < p2:
    print("두 번째 참가자의 승리입니다")
else:
    print("비겼습니다")