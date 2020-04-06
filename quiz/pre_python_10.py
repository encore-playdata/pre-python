"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

"""재귀함수 이용
number = int(input('자연수를 입력해주세요 : '))
def factorial(number):
    if number > 1:
        return number*factorial(number-1)
    else:
        return 1

print(factorial(number))
"""
def factorial(number):
    a = 1
    for i in range(1, number+1):
        a = a * i
    return a
number = int(input('자연수를 입력해주세요 : '))

print(factorial(number))
