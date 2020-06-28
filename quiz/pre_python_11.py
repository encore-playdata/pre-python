"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(x, y):
    for i in range(min(x,y), 0, -1):
        if x%i == 0 and y%i == 0:
            return i
    return -1
print(gcd(12,6))
