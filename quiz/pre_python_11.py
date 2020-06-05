"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(x, y):
    r = x % y
    if r == 0: return y
    else: return gcd(y, r)

print(gcd(12, 6))