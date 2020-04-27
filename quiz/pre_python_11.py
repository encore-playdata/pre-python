"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
"유클리드 호제법 이용"

def gcd(a,b):
    return b if a%b==0 else gcd(b, a%b)

print(gcd(12,6))
