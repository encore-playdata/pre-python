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
  ret = 1
  for i in range(1, num + 1):
    ret = ret * i
  return ret

number = int(input("입력 값: "))

print(factorial(number))

'''
또는 재귀호출법
def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)  
'''