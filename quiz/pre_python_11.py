"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""


def gcd(a, b):
    """
    유클리드 호제법을 참고함
    https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
    """
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd(12, 6))
