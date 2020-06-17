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
    __slots__ = '_balance', '_withdrawal_record'

    def __init__(self):
        self._balance = 0
        self._withdrawal_record = list(tuple())

    def charge(self, cost):
        self._balance += cost

    def check_dc(self, charge, used_for):
        if used_for == '영화관':
            return math.ceil(charge*0.8)

    def consume(self, charge, used_for = None ):
        used_for = self.check_dc(charge, used_for)
        if charge > self._balance:
            print('잔액이 부족합니다.')
            return
        self._withdrawal_record.append((used_for, charge))
        print('{}에서 {}원 사용했습니다.'.format(used_for, charge))

    def print(self):
        print('--잔액이 {}원입니다--'.format(self._balance))
        for i, c in enumerate(self._withdrawal_record):
            print('{} {} : {}'.format(i, c[0], c[1]))


def main():
    card = Card()
    card.charge(20000)
    card.consume(3000,'마트')
    card.consume(10000,'영화관')
    card.consume(13000,'마트')
    card.print()

if __name__ == '__main__':
    main()