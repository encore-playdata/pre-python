"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """
def factorial(n):
    if n == 0 or n == 1 :
        return 1
    if n == 2:
        return 2
    return n * factorial(n-1)


print(factorial(5))