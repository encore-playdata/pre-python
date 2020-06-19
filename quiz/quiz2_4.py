'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''

class Discount():
    def check_dc(self, charge, used_for):
        if used_for == '영화관': return charge * 0.8
        elif used_for == '마트': return charge * 0.9
        elif used_for == '교통': return charge * 0.9
        else:                   return charge * 1.0


class Card(Discount):
    def __init__(self):
        self._balance = 0

    def charge(self, deposit):
        self._balance += deposit

    def consume(self, charge, used_for):
        charge = self.check_dc(charge, used_for)
        if charge > self._balance:
            print('잔액이 부족합니다.')
            return
        print('{}에서 {}원 사용했습니다.'.format(used_for, charge))
        self._balance -= charge

    def print(self):
        print('잔액이 {}원 입니다.'.format(self._balance))


def main():
    multi_card=Card()
    multi_card.charge(20000)
    multi_card.consume(5000,'마트')
    multi_card.consume(10000,'영화관')
    multi_card.consume(2000,'교통')
    multi_card.print()

