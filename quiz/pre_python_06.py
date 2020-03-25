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

line = int(input("수를 입력하세요: "))

for star in range(1, line+1):
    print(' ' * (line - star) + '★' * ( 2 * star -1))

    if line == star:
        for star in range(line-1, 0, -1):
            print(' ' * (line - star) + '★' * (2 * star -1))





