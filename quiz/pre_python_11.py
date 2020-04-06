"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(x, y):

    lst_cd = []

    for n in range(1, max(x,y)+1):
        if x % n == 0 and y % n == 0:
            lst_cd.append(n)

    num_gcd = max(lst_cd)

    return num_gcd


print(gcd(12, 6))
