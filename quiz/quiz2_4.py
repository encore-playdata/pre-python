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
        self.amount = 0
        print("카드가 발급 되었습니다.")

    def charge(self, chg_amt):
        self.amount += chg_amt
        print('잔액이', self.amount ,'원 입니다.')

    def consume(self, csm_amt, place):
        if self.amount >= csm_amt :
            self.amount -= csm_amt
            print(place ,'에서', csm_amt,'원 사용했습니다.')
        else:
            print("잔액이 부족합니다.")            

    def print(self):
        print('잔액이', self.amount, '원 입니다.')


class Movie_card(Card):
    def consume(self, csm_amt, place):
        if place == '영화관' :
            csm_amt = int(csm_amt * .8)
        super().consume(csm_amt, place)

class Mart_card(Card):
    def consume(self, csm_amt, place):
        if place == '마트' :
            csm_amt = int(csm_amt * .9)
        super().consume(csm_amt, place)

class Traffic_card(Card):
    def consume(self, csm_amt, place):
        if place == '교통' :
            csm_amt = int(csm_amt * .9)
        super().consume(csm_amt, place)

class Multi_card(Card):
    def consume(self, csm_amt, place):
        if place == '영화관' :
            csm_amt = int(csm_amt * .8)        
        elif place == '교통' :
            csm_amt = int(csm_amt * .9)
        elif place == '마트' :
            csm_amt = int(csm_amt * .9)            

        super().consume(csm_amt, place)

print("영화카드")
movie_card=Movie_card()
movie_card.charge(20000)
movie_card.consume(5000,'마트')
movie_card.consume(10000,'영화관')
movie_card.consume(2000,'교통')
movie_card.print()        
print("")

print("마트카드")
mart_card=Mart_card()
mart_card.charge(20000)
mart_card.consume(5000,'마트')
mart_card.consume(10000,'영화관')
mart_card.consume(2000,'교통')
mart_card.print()   
print("")

print("교통카드")
traffic_card=Traffic_card()
traffic_card.charge(20000)
traffic_card.consume(5000,'마트')
traffic_card.consume(10000,'영화관')
traffic_card.consume(2000,'교통')
traffic_card.print()   
print("")

print("멀티카드")
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()
