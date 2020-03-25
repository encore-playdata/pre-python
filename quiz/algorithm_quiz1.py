'''
1.
팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다.
팩토리얼을 함수(factorial)로 구현하는데 재귀함수를 이용하여 구현하시오.

<입력>
print(factorial(10))

<출력>
3628800
'''

'''
#조건문을 너무 과도하게 넣었다. 
def factorial(n):
    if n == 1 : return 1
    elif n == 0 : return 1
    else: return n * factorial(n-1)
'''

'''
#조건문의 순서가 바뀌어서 n < 2라는 다소 깔끔하지 못한 조건이 들어감. . 
def factorial(n):
    if n < 2: return 1
    else: return n * factorial(n-1)
'''


# 삼항연산자를 활용하고 n > 1일때 재귀함수를 부르는 방식으로 변경. 더 깔끔해졌다.
def factorial(n):
    return n * factorial(n-1) if n > 1 else 1


print(factorial(10))
