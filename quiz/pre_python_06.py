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

n = int(input("숫자를 입력하세요 : "))

t = n
for i in range(t):
    for k in range(t - 1):
        print(" ", end = "")

    for k in range(i + 1):
        print("★", end = "")
    t -= 1
    print("")

t = n
for i in range(t):
    for k in range(i + 1):
        print(" ", end = "")

    for k in range(t - 1):
        print("★", end="")
    t -= 1
    print("")