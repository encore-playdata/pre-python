"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""


def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    return gcd(b, a % b) if a % b != 0 else b


print(gcd(12, 16))
