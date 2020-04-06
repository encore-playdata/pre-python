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

class MovieCard():
    def __init__(self):
        self.balance = 0

    def consume(self, payment, location):
        if location == "영화관":
            discount = payment*0.8
            if self.balance - discount <0:
                print("잔액이 부족합니다.")
            else:
                self.balance-=discount
                print("{}에서 {}원을 사용했습니다.".format(location, discount))
        else:
            self.balance-=payment
            print("{}에서 {}원을 사용했습니다.".format(location, payment))


class MartCard():

    def __init__(self):
        self.balance = 0


    def consume(self, payment, location):
        if location == "마트":
            discount = payment * 0.9
            if self.balance - discount < 0:
                print("잔액이 부족합니다.")
            else:
                self.balance -= discount
                print("{}에서 {}원을 사용했습니다.".format(location, discount))
        else:
            self.balance -= payment
            print("{}에서 {}원을 사용했습니다.".format(location, payment))

class TransCard():

    def __init__(self):
        self.balance = 0

    def consume(self, payment, location):
        if location == "교통":
            discount = payment * 0.9
            if self.balance - discount < 0:
                print("잔액이 부족합니다.")
            else:
                self.balance -= discount
                print("{}에서 {}원을 사용했습니다.".format(location, discount))
        else:
            self.balance -= payment
            print("{}에서 {}원을 사용했습니다.".format(location, payment))

class Multi_card(MovieCard,MartCard,TransCard):
    def __init__(self):
        self.balance = 0
        print('카드가 발급 되었습니다.')
    def consume(self, payment, location):
        if location == '영화관':
            MovieCard.consume(self, payment, location)
        elif location == '마트':
            MartCard.consume(self, payment, location)
        elif location == '교통':
            TransCard.consume(self,payment,location)
        else:
            super().consume(self, payment, location)

    def charge(self, deposit):
        self.balance+=deposit
        print('{}이 충전되었습니다.'.format(deposit))
    def print(self):
        print('잔액이 {}원입니다.'.format(self.balance))

multi_card = Multi_card()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()