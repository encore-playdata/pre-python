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
class Card():
    def __init__(self):
        self.balance = 0
        print('카드가 발급 되었습니다.')

    def print(self):
        print(f'잔액이 {self.balance}원 입니다.')

    def charge(self, deposit):
        self.balance += deposit
        print(f'{deposit}원이 충전되었습니다.')

    def consume(self, cost, place):
        if self.balance < cost:
            print('잔액이 부족합니다.')
            return
        else:
            self.balance -= cost
            print(f'{place}에서 {cost}원 사용했습니다.')

class Movie_card(Card):
    def consume(self, cost, place):
        if place == '영화관':
            cost *= 0.8
        super().consume(cost, place)

class Mart_card(Card):
    def consume(self, cost, place):
        if place == '마트':
            cost *= 0.9
        super().consume(cost, place)

class Traffic_card(Card):
    def consume(self, cost, place):
        if place == '교통':
            cost *= 0.9
        super().consume(cost, place)

class Multi_card(Mart_card, Movie_card, Traffic_card):
    def consume(self, cost, place):
        if place == '영화관':
            Movie_card.consume(self, cost, place)
        if place == '마트':
            Mart_card.consume(self, cost, place)
        if place == '교통':
            Traffic_card.consume(self, cost, place)

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()