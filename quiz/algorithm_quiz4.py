'''
4.
탐욕 알고리즘은 최적해를 구하는 상황에서 사용하는 방법입니다.
여러 경우 중 하나를 선택할 때 그것이 그상황에서 가장 좋다고 생각하는 것을
선택해 나가는 방식으로 진행하여 답을 구합니다.
하지만 탐욕알고리즘은 그 상황에서 가장 좋다고 생각하는 것을 선택해 나가는
방식이기 때문에 가장 좋은 결과를 얻는 것이 보장되는것은 아닙니다.
탐욕 알고리즘을 이용하여 동전을 지불하는 함수(greedy)를 짜는데 지불해야 하는
동전의 갯수가 최소가 되도록 함수를 구현하시오
(input 으로 액수와 동전의 종류를 입력하게 구현)

<입력>
print(greedy())

<출력>
액수입력 :  1050
동전의 종류 :  100 50 10
100원 동전 10개, 50원 동전 1개, 10원 동전 0개
'''
# 연산 순서에 따라서 값이 달라짐을 주의 할 것그리고 None은 왜 나오는 거지???
def greedy():
    money = int(input("액수입력 :  "))
    coin_catagory = input("동전의 종류 : ").split(" ")

    for coin_price in coin_catagory:
        coin_number = int(money // int(coin_price))
        print(f"{coin_price}원 동전 {coin_number}개", end=", ")
        money = money - (int(coin_price) * int(coin_number)) # 이값이 1050 원이라면 - 1000원을 뺀 50원
print(greedy())
