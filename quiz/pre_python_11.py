"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
number = int(input('최대공약수를 구할 자연수를 입력하세요 :'))

i = number//2
while i > 1:
    if number%i == 0:
        print ('{}는/은 {}의 최대공약수 입니다.'.format(i, number))
        break
    else:
        i-=1
