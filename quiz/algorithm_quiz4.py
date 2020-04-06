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

coin = list(map(int, input('동전의 종류를 입력해 주세요.:').split()))
change = int(input('거스름 돈을 입력해주세요 :'))

def greedy(change, coin):
    coin.sort(reverse=True)
    i = 0
    solution = 0
    result= {}
    first_change = change
    while change != 0:
        if change > coin[i]:
            change -=coin[i]
            solution +=1
        elif change == coin[i]:
            change-=coin[i]
            solution = 1
            result[coin[i]] = solution
        else:
            result[coin[i]] = solution
            i+=1
            solution = 0

    print('액수 입력 : {}'.format(first_change))
    print('동전의 종류 : ', end = '')
    print(",".join(map(str, coin)))
    for i in range(len(coin)):
        if i !=len(coin)-1:
            if coin[i] in result:
                print('{}원 동전 {}개, '.format(coin[i], result[coin[i]]), end = '')
            else:
                print('{}원 동전 0개, '.format(coin[i]), end = '')
        else:
            if coin[i] in result:
                print('{}원 동전 {}개'.format(coin[i], result[coin[i]]))
            else:
                print('{}원 동전 0개'.format(coin[i]))
    return''

print(greedy(change, coin))
