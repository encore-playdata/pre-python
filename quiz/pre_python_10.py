"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """


def factorial(num):
    if num == 1:
        return 1
    if num <= 0:
        raise ValueError("입력 숫자는 1보다 커야합니다.")
    return num * factorial(num-1)


print(factorial(5))
