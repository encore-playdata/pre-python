"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(number1, number2):
    temp = []
    for i in range(1, max(number1, number2) + 1):
        if number1 % i == 0 and number2 % i == 0:
            temp.append(i)

    return max(temp)

print(gcd(12, 6))
