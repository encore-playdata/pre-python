"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd1(num1,num2):
    num1_cd = [i for i in range(1,num1+1) if num1 % i ==0]
    gcd = [cd for cd in num1_cd if num2 % cd == 0][-1]
    return gcd

def gcd2(num1,num2):
    return num2 if num1%num2 == 0 else gcd(num2,num1%num2)
print(gcd1(12,6))
print(gcd2(12,6))