"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 5

<출력>
    ★
   ★★
  ★★★
 ★★★★
★★★★★  
 ★★★★
  ★★★
   ★★
    ★


"""
number = int(input('숫자를 입력하세요 : '))
space = " "
star = "★"
for i in range(number):
    print(space*(number -1 - i) + star*(i + 1))
for i in range(number - 1):
    print(space*(i + 1) + star*(number - i - 1))