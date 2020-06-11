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
    '''카드'''

    def __init__(self):
        '''초기화 함수'''
        self.amount = 0

    def charge(self, amount):
        self.amount += amount
        print("{}원이 충전되었습니다.".format(amount))

    def consume(self, amount, location):
        pass

    def print(self):
        print("잔액이 {}원 입니다.".format(self.amount))


class MovieCard(Card):

    def consume(self, amount, location):
        super().consume(amount, location)
        if location == "영화관":
            sales = amount * 0.8
            self.amount -= sales
            print("{}에서 {}원을 사용했습니다.".format(location, sales))


class MartCard(Card):

    def consume(self, amount, location):
        super().consume(amount, location)
        if location == "마트":
            sales = amount * 0.9
            self.amount -= sales
            print("{}에서 {}원을 사용했습니다.".format(location, sales))


class TransCard(Card):

    def consume(self, amount, location):
        super().consume(amount, location)
        if location == "교통":
            sales = amount * 0.9
            self.amount -= sales
            print("{}에서 {}원을 사용했습니다.".format(location, sales))


class Multi_card(MovieCard, MartCard, TransCard):
    def __init__(self):
        super().__init__()
        print("카드가 발급되었습니다.")

    def consume(self, amount, location):
        super().consume(amount, location)
        if location == "마트" or location == "영화관" or location == "교통":
            pass
        elif self.amount < amount:
            print("잔액이 부족합니다.")
        else:
            self.amount -= amount
            print("{}에서 {}원을 사용했습니다.".format(location, amount))


multi_card = Multi_card()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()