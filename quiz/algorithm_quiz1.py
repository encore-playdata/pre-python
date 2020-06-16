'''
1.
팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다.
팩토리얼을 함수(factorial)로 구현하는데 재귀함수를 이용하여 구현하시오.

<입력>
print(factorial(10))

<출력>
3628800'''

def factorial(n): 
    if n == 1: return 1 
    dp_arr = [0, 1] 

    for i in range(2, n+1): 
        dp_arr.append(dp_arr[-1]*i)
    print(dp_arr)
    return dp_arr[n]

print(factorial(10)) 
