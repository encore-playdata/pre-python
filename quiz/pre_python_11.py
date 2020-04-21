"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a, b):
    if b > a: a, b = b, a   # 큰 수를 a에 저장
    return b if a % b == 0 else gcd(b, a % b)