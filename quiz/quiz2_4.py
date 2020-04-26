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

class movie_card:
    def movie(self):
        return 0.8

class market_card:
    def market(self):
        return 0.9

class traffic_card:
    def traffic(self):
        return 0.9

class Multi_card(movie_card, market_card, traffic_card):
    total = 0
    print('카드가 발급 되었습니다')
    def charge(self, money):
        self.total += money
        print(f'{money}이 충전되었습니다.')

    def consume(self, money, place):
        if place == '마트':
            money = money * self.market()
        elif place == '영화관':
            money = money * self.movie()
        elif place == '교통':
            money = money * self.traffic()
        if self.total - money >= 0:
            self.total -= money
            print(f'{place}에서 {money}원을 사용했습니다.')
        else:
            print("잔액이 부족합니다")

    def print(self):
        print(f'잔액이 {self.total}입니다')

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()