"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(a, b):
    if (a < b):
        a, b = b, a
    if (b == 0):
        return a
    if (a % b == 0):
        return b
    else:
        return gcd(b, a%b)

print(gcd(12, 6))

