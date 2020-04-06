"""
11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))
<출력>
6
"""
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(12,6))