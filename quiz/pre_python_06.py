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

x = input("숫자를 입력하세요 : ")
for i in range(int(x)):
    print((int(x) - i) * " ", end="")
    print("{}".format("★" * (i + 1)))
for i in range(int(x) - 1, 0, -1):
    print((int(x) - i + 1) * " ", end="")
    print("{}".format("★" * i))
