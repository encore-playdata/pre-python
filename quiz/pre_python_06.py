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
"""

x = int(input("숫자를 입력하세요"))
for i in range(1,2*x):
    for j in range(0,abs(x-i)):
        print(" ",end="")
    if(i<=x):
        for k in range(i,0,-1):
            print("★",end="")
    else:
        for k in range(x-abs(x-i),0,-1):
            print("★",end="")
    print('')

