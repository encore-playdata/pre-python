"""
1. 재귀 호출을 이용한 <피보나치 수열> 함수 만들기 문제

피보나치 수열이란 첫 번째 항과 두 번째 항이 1이고, 세 번째 항부터는 바로 앞의 두 항의 합으로 정의된 수열입니다.
예를 들어서 세 번째 항은 첫 번째 항(1)과 두 번째 항(1)을 더한 2이며, 네 번째 항은 두 번째 항(1)과 세 번째 항(2)을 더한 3이 될 것입니다.
파라미터로 1 이상의 자연수 **`n`**을 받고, n번째 피보나치 수를 리턴하는 재귀 함수 fibonacci 함수를 작성하세요.
예를 들어 n = 3이라면 2를 반환해주면 됩니다.

입력 예시)
print(fibonacci(10))

출력 결과)
55
"""

def fibonacci(n):
    result = []
    for i in range(0, n):
        if i <= 1:
            result.append(1)
        else:
            result.append(result[i-2] + result[i-1])
    return result[-1]

print(fibonacci(10))