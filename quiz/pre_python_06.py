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

drawing_star = int(input('숫자를 입력하세요 :'))
space = " "
space_count = drawing_star

for star_count in range(drawing_star):
    star_count += 1
    space_count -= 1
    print(space * space_count + star_count * "★")

for star_count in range(drawing_star, 0, -1):
    star_count -= 1
    space_count += 1
    print(space * space_count + star_count * "★")