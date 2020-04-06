'''
1.
팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다.
팩토리얼을 함수(factorial)로 구현하는데 재귀함수를 이용하여 구현하시오.

<입력>
print(factorial(10))

<출력>
3628800'''
# 탬프를 사용하는게 아니라 말그대로 함수안에 함수를 사용하는 거구나.. 반복문을 사용하지 않고 함수안에 함수를 사용하는 방법으로

i = 0
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(10))



