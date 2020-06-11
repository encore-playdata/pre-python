"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factorial(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

def factorial(number):
    facto = 1
    for num in range(1,number+1):
        facto *= num
    return(facto)
    
print(factorial(5))