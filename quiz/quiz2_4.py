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
    def consume(self, price, place):
        if self.money >= price:
            if place == '영화관':
                self.money -= price*0.8
                print('{}에서 {}원을 사용했습니다.'.format(place, price*0.8))
            elif place == '마트':
                self.money -= price*0.9
                print('{}에서 {}원을 사용했습니다.'.format(place, price*0.9))
            elif place == '교통':
                self.money -= price*0.9
                print('{}에서 {}원을 사용했습니다.'.format(place, price*0.9))
            else:
                self.money -= price
                print('{}에서 {}원을 사용했습니다.'.format(place, price))
        else:
            print('잔액이 부족합니다.')


class Multi_card(Discount):
    def __init__(self):
        self.money = 0
        print('카드가 발급 되었습니다')

    def charge(self, money):
        self.money += money
        print('{}이 충전되었습니다.' .format(money))

    def print(self):
        print('잔액이 {}원 입니다.' .format(self.money))

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()