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

import math


class Card(object):
    def __init__(self):
        self._balance = 0

    def charge(self, cost):
        self._balance += cost
        print('잔액이 {}원 입니다.'.format(self._balance))

    def check_dc(self, charge, used_for):
        if used_for == '영화관': return int(charge * 0.8)
        else: return int(charge * 1.0)

    def consume(self, charge, used_for = None ):
        charge = self.check_dc(charge, used_for)
        if charge > self._balance:
            print('잔액이 부족합니다.')
            return
        print('{}에서 {}원 사용했습니다.'.format(used_for, charge))
        self._balance -= charge

    def print(self):
        print('잔액이 {}원입니다'.format(self._balance))


def main():
    card = Card()
    card.charge(20000)
    card.consume(3000,'마트')
    card.consume(10000,'영화관')
    card.consume(13000,'마트')
    card.print()
    

main()
