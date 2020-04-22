"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(a, b):
    if a >= b:
        r = range(a,0,-1)
    else:
        r = range(b,0,-1)
    for i in r:
        if (a % i == 0) and (b % i == 0):
            print(i)
            break

gcd(12,6)
