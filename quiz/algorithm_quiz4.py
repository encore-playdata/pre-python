'''
4.
탐욕 알고리즘은 최적해를 구하는 상황에서 사용하는 방법입니다.
여러 경우 중 하나를 선택할 때 그것이 그상황에서 가장 좋다고 생각하는 것을
선택해 나가는 방식으로 진행하여 답을 구합니다.
하지만 탐욕알고리즘은 그 상황에서 가장 좋다고 생각하는 것을 선택해 나가는
방식이기 때문에 가장 좋은 결과하는 함수(greedy)를 짜는데 지불해야 하는
동전의 갯수가 최소가 되도록 함수를 구를 얻는 것이 보장되는것은 아닙니다.
탐욕 알고리즘을 이용하여 동전을 지불현하시오
(input 으로 액수와 동전의 종류를 입력하게 구현)

<입력>
print(greedy())

<출력>
액수입력 :  1050
동전의 종류 :  100 50 10
100원 동전 10개, 50원 동전 1개, 10원 동전 0개
'''

def greedy():
    money = int(input("액수입력: "))
    coin1, coin2, coin3 = map(int, input("동전의 종류: ").split())
    coin1_count = 0
    coin2_count = 0
    coin3_count = 0
    while(money):
        if money >= coin1 :
            money -= coin1
            coin1_count += 1
        elif money >= coin2 :
            money -= coin2
            coin2_count += 1
        elif money >= coin3 :
            money -= coin3
            coin3_count += 1
    return '{}원 동전 {}개, {}원 동전 {}개, {}원 동전 {}개'.format(coin1,coin1_count,coin2,coin2_count,coin3,coin3_count)

print(greedy())