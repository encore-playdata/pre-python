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
class Card:
    def __init__(self):
        self.result = 0
        print('카드가 발급 되었습니다.')

    def charge(self, num):
        self.result += num
        print('{}이 충전되었습니다.'.format(num))

    def print(self):
        print('잔액이 {}원 입니다'.format(self.result))

class Movie_card(Card):
    def consume(self, num, place):
        if place == '영화관':
            if self.result - num * 0.8 < 0:
                print('잔액이 부족합니다.')
            else:
                self.result -= num * 0.8
                print('{}에서 {}원을 사용했습니다.'.format(place, num * 0.8))

class Mart_Transit_card(Card):
    def consume(self, num, place):
        if place in ['마트', '교통']:
            if self.result - num * 0.9 < 0:
                print('잔액이 부족합니다.')
            else:
                self.result -= num * 0.9
                print('{}에서 {}원을 사용했습니다'.format(place, num * 0.9))

class Multi_card(Movie_card, Mart_Transit_card):
    def consume(self, num, place):
        if place == '영화관':
            Movie_card.consume(self, num, place)
        elif place in ['마트', '교통']:
            Mart_Transit_card.consume(self, num, place)
        else:
            if self.result - num < 0:
                print('잔액이 부족합니다.')
            else:
                self.result -= num
                print('{}에서 {}원을 사용했습니다.'.format(place, num))

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()