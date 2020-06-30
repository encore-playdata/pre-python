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

n = input('숫자를 입력하세요 : ')
space = ' '
star = '★'


for i in range(int(n), 0, -1):
    print(space * (i-1), end='')
    print(star * (int(n) - (i - 1)))
    if i == 1:
        for j in range(1, int(n)):
            print(space * j, end='')
            print(star * (int(n) - j))