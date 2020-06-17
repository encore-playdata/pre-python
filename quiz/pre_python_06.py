"""6. 아래와 같이 별이 찍히게 출력하시오.

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
number_star = int(input("숫자를 입력하세요 : "))

for i in range(number_star):
    print(' '*(number_star-i-1)+'★'*(i+1))
for j in range(number_star-1,0,-1):
    print(' '*(number_star-j)+'★'*(j))