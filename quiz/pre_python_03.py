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

fir_input = input('첫 번째 참자가 엔터키를 눌러 주사위를 던져 주세요 : ')

if fir_input == '':
    fir_num = random.randrange(1, 6)
    print(fir_num)

sec_input = input('두 번째 참자가 엔터키를 눌러 주사위를 던져 주세요 : ')

if sec_input == '':
    sec_num = random.randrange(1, 6)
    print(sec_num)

if fir_num > sec_num:
    print('첫 번째 참가자의 승리입니다.')
elif fir_num == sec_num:
    print('비겼습니다.')
else:
    print('두 번째 참가자의 승리입니다.')