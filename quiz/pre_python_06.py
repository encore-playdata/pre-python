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

star_num = int(input("숫자를 입력하세요 : "))
space_num = star_num
i = 0

for i in range(star_num - i):
    for j in range(space_num - 1):
        print(" ", end='')
    for j in range(0, i + 1):
        print("★", end="")
    print()
    space_num -= 1

for i in range(star_num):
    for j in range(space_num + 1):
        print(" ", end='')
    for j in range(i, star_num - 1):
        print("★", end="")
    print()
    space_num += 1
