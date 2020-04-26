"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a,b):
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(30,18))
