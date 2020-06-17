"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(n, m):
    gcd = 0
    for i in range(1, min(m,n) + 1):
        if m % i == 0 and n % i == 0: gcd = i
    return gcd

print(gcd(12,6))