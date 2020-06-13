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


a = int(input("숫자를 입력하세요 : "))
b = "★"

for i in range(1, a+1):
    inp = b * i
    inp = inp.rjust(a)
    print(inp)
    if i == 5:
        i = i - 1
        for i in range(a-1, 0, -1):
            inp = b * i
            inp = inp.rjust(a)
            print(inp)

