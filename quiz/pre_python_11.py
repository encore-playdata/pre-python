"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a, b):
    condition = True
    if a > b:
        k = b
    else:
        k = a
    while condition:
        if (a%k==0) & (b%k==0):
            condition = False
            return k
        k -= 1
