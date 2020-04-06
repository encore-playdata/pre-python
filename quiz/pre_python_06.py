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

def make_dia():
    input_number = int(input("숫자를 입력하세요 : "))
    input_list = list(range(1, input_number)) + list(range(input_number, 0, -1))

    for i in input_list:
        print(" "*(input_number-i), "★"*i)


make_dia()
