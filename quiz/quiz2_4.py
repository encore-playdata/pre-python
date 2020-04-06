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
        self.my_money = 0

    def charge(self, charge_money):
        self.my_money += charge_money
        print("잔액이 {}원 입니다.".format(self.my_money))

    def consume(self, consume_money, where):
        if self.my_money >= consume_money:
            self.my_money -= consume_money
            print("{}에서 {}원 사용했습니다.".format(where, consume_money))

        else:
            print("잔액이 부족합니다.")

    def print(self):
        print("잔액이 {}원 입니다.".format(self.my_money))

class Transportation_card(Card):
    def consume(self, consume_money, where):
        if where == "교통":
            consume_money *= 0.9
            consume_money = int(consume_money)

        super().consume(consume_money, where)


class Movie_card(Card):
    def consume(self, consume_money, where):
        if where == "영화관":
            consume_money *= 0.8
            consume_money = int(consume_money)

        super().consume(consume_money, where)

class Mart_card(Card):
    def consume(self, consume_money, where):
        if where == "마트":
            consume_money *= 0.9
            consume_money = int(consume_money)

        super().consume(consume_money, where)


class Multi_card(Transportation_card, Movie_card, Mart_card):
    def __init__(self):
        super().__init__()
        print("카드가 발급 되었습니다.")

    def consume(self, consume_money, where):
        if where == "교통":
            Transportation_card.consume(self, consume_money, where)

        elif where == "마트":
            Mart_card.consume(self, consume_money, where)

        elif where == "영화관":
            Movie_card.consume(self, consume_money, where)

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()
