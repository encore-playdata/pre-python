"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a,b):
  for i in range(a, 0, -1):
    if a % i == 0 and b % i== 0:
      return i