"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""


def gcd(x, y):
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


print(gcd(12, 30))