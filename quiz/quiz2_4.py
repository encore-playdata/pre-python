"""
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card = MultiCard()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500원을 사용했습니다.
영화관에서 8000원을 사용했습니다.
교통에서 1800원을 사용했습니다.
잔액이 5700원 입니다
"""


class Card:
    _balance = 0

    def __init__(self):
        print("카드가 발급 되었습니다.")

    def charge(self, amount):
        self._balance += amount
        print(f"{self._balance}원이 충전되었습니다.")

    def consume(self, amount, where):
        if self._balance < amount:
            print("잔액이 부족합니다")
            return

        self._balance -= amount
        print(f"{where}에서 {amount}원을 사용했습니다.")

    def print(self):
        print(f"잔액이 {self._balance}원 입니다.")


class Discount:
    _movie = 0.8
    _mart = 0.9
    _transportation = 0.9

    def apply_discount(self, amount, where):
        if where == "영화관":
            return int(amount * self._movie)
        if where == "마트":
            return int(amount * self._mart)
        if where == "교통":
            return int(amount * self._transportation)

        return amount


class MultiCard(Card, Discount):
    def consume(self, amount, where):
        amount = self.apply_discount(amount, where)
        super().consume(amount, where)


multi_card = MultiCard()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()
