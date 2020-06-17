"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

def factorial(k):
    if k == 1:
        return 1
    return k*factorial(k-1)

def main():
    k = int(input('숫자 입력 : '))
    print(factorial(k))

main()