"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(a, b):
    if a > b:
        smaller_number = b
    else:
        smaller_number = a

    for i in range(1, (smaller_number + 1)):
        if a % i == 0 and b % i == 0:
            result = i

    return result

print(gcd(12, 6))