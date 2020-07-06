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

number = int(input("숫자를 입력하세요 : "))

reverse = False
stars = 1

while 0 < stars:
    for i in range(number - stars):
        print(' ', end='')
    for i in range(stars):
        print('★', end='')
    print()

    if stars == number:
        reverse = True

    if not reverse:
        stars += 1
    else:
        stars -= 1
