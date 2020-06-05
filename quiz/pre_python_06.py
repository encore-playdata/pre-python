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

def dmakeADiamond(Number):
    i = 0
    j = Number
    while i < Number:
        i = i + 1
        print(('★' * i).center(Number))
    while 0 < j:
        j = j - 1
        print(('★' * j).center(Number))


Number = int(input("숫자를 입력하세요 : "))

dmakeADiamond(Number)