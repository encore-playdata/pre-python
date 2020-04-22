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
number = int(input("숫자를 입력하세요  : "))
for i in range (number):
    for j in range(number, i, -1 ) :
        print(' ', end='')
    for k in range(i + 1):
        print('★ ', end='')
    print('')    
for i in range (number -1, 0, -1):
    for j in range(number - i + 1) :
        print(' ', end='')
    for k in range(i):
        print('★ ', end='')
    print('')    