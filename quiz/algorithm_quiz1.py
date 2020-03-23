'''
1.
팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다.
팩토리얼을 함수(factorial)로 구현하는데 재귀함수를 이용하여 구현하시오.

<입력>
print(factorial(10))

<출력>
3628800'''


def factorial(num):
    if num == 1:
        return 1
    if num <= 0:
        raise ValueError("입력 숫자는 1보다 커야합니다.")
    return num * factorial(num-1)


print(factorial(10))
