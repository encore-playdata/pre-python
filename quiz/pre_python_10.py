"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

def factorial(number):

    number_list = list(range(number, 1, -1))

    result = 1

    for i in number_list:
        result *= i

    return result

print(factorial(4))

