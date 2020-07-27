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


num1 = 0
num2 = 0
place = ""


class Multi_card:

    def __init__(self):
        self.result = num1


    def charge(self, num1):
        self.result += num1
        print("카드가 발급 되었습니다.")
        print(str(num1) + "이 충전되었습니다.")

    def consume(self, num2, place):
        if place == "영화관":
            self.result = self.result - (num2 - (num2 * 0.2))
            print(place + "에서 " + str(num2 - (num2 * 0.2)) + "원을 사용했습니다.")

        if place == "교통":
            self.result = self.result - (num2 - (num2 * 0.1))
            print(place + "에서 " + str(num2 - (num2 * 0.1)) + "원을 사용했습니다.")

        if place == "마트":
            self.result = self.result - (num2 - (num2 * 0.1))
            print(place + "에서 " + str(num2 - (num2 * 0.1)) + "원을 사용했습니다.")

    def print(self):
        print("잔액이 " + str(self.result) + "원 입니다")


multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()
