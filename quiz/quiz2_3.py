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


# 한 객체에 대한 인스턴스를 생성할 때 호출되는 것이 __init__ 함수
# __init__ 함수를 사용하면 클래스명을 쓰고 옆에 바로 인자들을 채워 넣음으로써, 그 값들을 지닌 객체를 만들어 낼 수 있음
# 파이썬에서는 class에서 사용하는 함수의 첫번째 인자(parameter)를 'self'로 사용하는 것이 원칙!
class Card():
    def __init__(self):
        self.money = 0

    # 충전 기능
    def charge(self, plus):
        self.money = self.money + plus
        print("잔액이 {}원 입니다.".format(self.money))

    # 소비 기능
    def consume(self, spend, place):
        if place == "영화관":  # 소비 장소가 '영화관'인 경우
            if self.money < spend * 0.8:
                print("잔액이 부족합니다.")
            else:
                self.money = self.money - spend * 0.8
                print("{}에서 {:.0f}원 사용했습니다.".format(place, spend * 0.8))
        else:  # 소비 장소가 '영화관'이 아닌 경우
            if self.money < spend:
                print("잔액이 부족합니다.")
            else:
                self.money = self.money - spend
                print("{}에서 {:.0f}원 사용했습니다.".format(place, spend))

    # 잔액을 출력해주는 print 기능
    def print(self):
        print("잔액이 {:.0f}원 입니다.".format(self.money))


card = Card()
card.charge(20000)
card.consume(3000, '마트')
card.consume(10000, '영화관')
card.consume(13000, '마트')
card.print()