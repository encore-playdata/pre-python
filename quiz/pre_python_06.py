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
n = int(input('숫자를 입력하세요 : '))
for i in range(0, n):
    for blank in range(0, n-i):
        print(" ", end = "")
    for star in range(0, i):
        print("★", end = "")
    print()
for i in range(0, n):
    for blank in range(0, i):
        print(" ", end = "")
    for star in range(0, n-i):
        print("★", end = "")
    print()
