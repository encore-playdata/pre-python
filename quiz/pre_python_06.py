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

a = input('숫자를 입력하세요 : ')

for i in range(1,int(a)+1):
    star = i * '★'
    print(star.rjust(int(a)))
for j in range(int(a)-1,0,-1):
    star2 = j * '★'
    print(star2.rjust(int(a)))
