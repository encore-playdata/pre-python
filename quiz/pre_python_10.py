"""
10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factorial(5)) -> 120 출력

예시
<입력>
print(factorial(5))

<출력>
120
  """
n = int(input("슷자를 입력하세요> "))
factorial = 1
i=1
while(i <= n):
    factorial = i * factorial
    i = i+1
print(factorial)