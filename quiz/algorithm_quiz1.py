"""
1.
팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다.
팩토리얼을 함수(factorial)로 구현하는데 재귀함수를 이용하여 구현하시오.

<입력>
print(factorial(10))

<출력>
3628800
"""


def factorial(n):   # 팩토리얼 def 함수 선언
    if n == 1:      # if n이 1 이라면
        return 1    # 1로 리턴
    return n * factorial(n - 1)  # 아니라면 n * 팩토리얼 n - 1로 리턴


print(factorial(10))
