"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""


def gcd(a, b):
    n = 1
    m = 2
    for i in range(1, a * b):
        if m > a or m > b:
            return n
        elif a % m >= 1 or b % m >= 1:
            m = m + 1
        elif a % m == 0 and b % m == 0:
            a = a // m
            b = b // m
            n = n * m


print(gcd(10241024, 20482048))
