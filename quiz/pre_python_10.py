"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """
"""
def Factorial(x) :
  for i in range(1,x+1):
    x= x*i

print(Factorial(3))
"""
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))