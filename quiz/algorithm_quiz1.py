'''
1.
팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다.
팩토리얼을 함수(factorial)로 구현하는데 재귀함수를 이용하여 구현하시오.

<입력>
print(factorial(10))

<출력>
3628800'''



def factorial(n):
    s = 1
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        for n in range(1,n+1):
            s = s * n
    return s

print(factorial(10))