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
    if number == 1:
        return 1
    elif number > 1:
        return number * factorial(number - 1)
    else:
        return '팩토리얼을 구할 수 없습니다.'