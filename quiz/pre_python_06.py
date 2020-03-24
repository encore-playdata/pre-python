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

x = int(input("숫자를 입력하세요 : "))

for i in range(x*2):
    if(i<=x):
        for j in range(x-i):
            print(" ", end="")
        for j in range(i):
            print("★", end="")
        print()
    else:
        for j in range(i-x):
            print(" ",end="")
        for j in range((x*2)-i):
            print("★",end="")
        print()

