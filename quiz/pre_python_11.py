"""
11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""


def gcd(i, j):  # 최대공약수 함수 선언
    while j != 0:   # j가 0이 아닐 때 반복
        i, j = j, i % j     # i에서 j를 j에 i에서 j를 나눈 나머지를 교환해서 저장
    return i    # i를 반환


print(gcd(12, 6))
