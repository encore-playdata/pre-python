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


"""1.클래스 카드 만들고
   2. 상속으로 영화, 마트, 교통에 적용한다. 
   3. 교통은 10% 할인이란다. 
   4. 마찬가지로 충전, 그리고 사용시 마이너스 마지막에 잔액 출력까지.
   상속 수업 실습 참고."""


class Multi_card():
    def __init__(self):
        self.money = 0

    def charge(self, num):
        self.money += num
        print("카드가 발급 되었습니다.")  #출력 내용을 추가한다.
        print("{}원이 충전되었습니다.".format(num))

    def consume(self, num, place):

        if place == "영화관":
            if self.money - num * 0.8 < 0:
                print('잔액이 부족합니다.')
            else:
                self.money -= num * 0.8
                print('{}에서 {:.0f}원 사용했습니다.'.format(place, num * 0.8))

        elif place == "마트":   # 마트에도 할인율 적용
            if self.money - num * 0.9 < 0:
                print('잔액이 부족합니다.')
            else:
                self.money -= num * 0.9
                print('{}에서 {:.0f}원 사용했습니다.'.format(place, num * 0.9))

        elif place == "교통": # 교통에도 할인율 적용
            if self.money - num * 0.9 < 0:
                print('잔액이 부족합니다.')
            else:
                self.money -= num * 0.9
                print('{}에서 {:.0f}원 사용했습니다.'.format(place, num * 0.9))

    def print(self):
        print('잔액이 {:.0f} 입니다.'.format(self.money))


multi_card = Multi_card()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()
