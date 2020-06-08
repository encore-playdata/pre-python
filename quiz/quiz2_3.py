'''
3.
Card 클래스를 생성해 카드에 충전기능, 소비기능, 잔액을 알려주는 기능을 넣으시오.
-충전기능 (charge)
-소비기능 (consume)
-영화관에서 카드를 사용하면 20% 할인율 적용
print 기능(print) # 잔액이 ( ) 원 입니다.

테스트코드
<입력>
card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()

<출력>
잔액이 20000원 입니다.
마트에서 3000원 사용했습니다.
영화관에서 8000원 사용했습니다.
잔액이 부족합니다
잔액이 9000원 입니다.
'''

'''1. 카드 클래스를 만든다.
    2. 함수 차지, 콘숨 만든다. 셀프, 가격, 사용처
    3. 프린트 한다. 단, 영화관에서는 20% 깎는 함수 지정
    4. 잔액은 더하기, 콘숨은 잔액에서 마이너스 적용
    5. 잔액이 부족할 때 프린트 "잔액이 부족합니다."
    6. 마지막에 잔액 출력'''


class Card():
    def __init__(self): #기본 뼈대를 만들고
        self.money = 0

    def charge(self, num): # 뼈대 위에 데이터를 얹는다. 출력까지 학습시키기
        self.money += num
        print("잔액이 {}원 입니다.".format(num))

    def consume(self, num, place): # 소비 함수를 만든다.

        if place == "영화관":   # 영화관은 할인 예외 적용, 부족한 것 먼저 조건을 거는 게 편하다.
            if self.money - num * 0.8 < 0:
                print('잔액이 부족합니다.')
            else:
                self.money -= num * 0.8
                print('{}에서 {:.0f}원 사용했습니다.'.format(place, num * 0.8))
        else:
            if self.money - num < 0: # 그 외 사용들은 동일한 조건으로
                print('잔액이 부족합니다.')
            else:
                self.money -= num
                print('{}에서 {:.0f}원 사용했습니다.'.format(place, num))

    def print(self):   # 잔액을 정리한다.
        print('잔액이 {:.0f} 입니다.'.format(self.money))


card = Card()
card.charge(20000)
card.consume(3000, '마트')
card.consume(10000, '영화관')
card.consume(13000, '마트')
card.print()