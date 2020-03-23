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


class movieCard():
    def __init__(self):
        self.money = 0

    def movie_consume(self, price):
        dis_price = price * 0.8
        return dis_price


class martCard():
    def __init__(self):
        self.money = 0

    def mart_consume(self, price):
        dis_price = price * 0.9
        return dis_price


class transCard():
    def __init__(self):
        self.money = 0

    def trans_consume(self, price):
        dis_price = price * 0.9
        return dis_price


class Multi_card(movieCard, martCard, transCard):
    def __init__(self):
        self.money = 0

    def charge(self, money):
        self.money += money
        print('{}원이 충전되었습니다.'.format(money))

    def print(self):
        print('잔액이 {}원 입니다.'.format(self.money))

    def consume(self, price, place):
        con_money = 0
        if place == '영화관':
            con_money = super().movie_consume(price)
        elif place == '마트':
            con_money = super().mart_consume(price)
        elif place == '교통':
            con_money = super().trans_consume(price)
        else:
            con_money = price
        if self.money < con_money:
            print('잔액이 부족합니다.')
            return
        self.money -= con_money
        print('{}에서 {}원 사용했습니다.'.format(place, con_money))


multi_card = Multi_card()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()
