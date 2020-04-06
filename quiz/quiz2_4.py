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
    # 카드마다 공통된 내용 입력하기, 카드발급, 충전, 잔액조회, 카드사용, 잔액 부족 또 있나?
    def __init__(self):
        self.amount = 0
    print("카드가 발급 되었습니다.")

    def charge(self, cha_price):
        self.cha_price = cha_price
        self.amount = self.amount + cha_price
        print("{}원이 충전되었습니다.".format(cha_price))

    def print(self):
        print("잔액이 {}원 입니다.".format(self.amount))

    def consume(self, cost, place):
        self.cost = cost
        self.place = place
        if self.amount >= cost:
            self.amount = self.amount - cost
            print("{}에서 {}원을 사용했습니다.".format(place, cost))
        else:
            print("잔액이 부족합니다.")

class Traffic_card(Card):

    def consume(self, cost, place):
        if place == "교통":
            cost = int(cost * 0.9)
            super().consume()

class Movie_card(Card):

    def consume(self, cost, place):
        if place == "영화관":
            cost = int(cost * 0.8)
            super().consume()

class Mart_card(Card):

    def consume(self, cost, place):
        if place == "마트":
            cost = int(cost * 0.9)
            super().consume()


class Multi_card(Card):

    def consume(self, cost, place):
        if place == "영화관":
            cost = int(cost * 0.8)
            super().consume(cost, place)
        if place == "마트":
            cost = int(cost * 0.9)
            super().consume(cost, place)
        if place == "교통":
            cost = int(cost * 0.9)
            super().consume(cost, place)


multi_card = Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()