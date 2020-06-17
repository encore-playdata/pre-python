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

def greedy_dude():
    price = int(input('액수 입력 : '))
    hundred, fifty, ten = map(int, input('100원, 50원, 10원 갯수 입력 : ').split() )
    hc = fc = tc = 0  # 동전 카운트
    sum = 0         #

    while hc < hundred and hc*100 < price and price > sum:
        hc += 1
        sum += 100

    while fc < fifty and fc*50 < price and price > sum:
        fc += 1
        sum += 50

    while tc < ten and tc*100 < price and price > sum:
        tc += 1
        sum += 10

    print('100원 : {}개, 50원 : {}개, 10원 : {}개'.format(hc, fc, tc))


def main():
    greedy_dude()



main()


