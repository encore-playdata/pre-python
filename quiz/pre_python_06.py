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

i=int(input("숫자를 입력하세요 : "))

for upper in range(i):
    for space in range(i-1-upper):
        print(" ",end="")
    for star in range(upper+1):
        print("★",end="")
    print("")
for lower in range(i-1):
    for space in range(lower+1):
        print(" ",end="")
    for star in range(i-lower-1):
        print("★",end="")
    print("")
