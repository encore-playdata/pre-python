"""
10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
"""


def factorial(n):   # 팩토리얼 def 함수 선언
    if n == 1:      # if n이 1 이라면
        return 1    # 1로 리턴
    return n * factorial(n - 1)  # 아니라면 n * 팩토리얼 n - 1로 리턴


print(factorial(5))
