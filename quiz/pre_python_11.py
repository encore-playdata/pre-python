"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a, b):
    gcd = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
           gcd = i
    return gcd

print(gcd(12,6))