"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(num1, num2):
    for i in range(num1, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i

number1 = int(input("입력 값1: "))
number2 = int(input("입력 값2: "))
print(gcd(number1,number2))