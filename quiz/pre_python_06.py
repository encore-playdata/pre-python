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

number = int(input('숫자를 입력하세요 :'))
for i in range(1,2*number):
    if i <= number:
        space = ' '*(number-i)
        star = '*'*i
        print('{}{}'.format(space,star))
    else:
        space = ' '*(i-number)
        star = '*'*(2*number-i)
        print('{}{}'.format(space,star))