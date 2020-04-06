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
print('<입력>')
number = int(input('숫자를 입력하세요 : '))

print()

print('<출력>')
for x in range(number) : 
    print(' '*(number-x) + '★ '*(x+1))

for y in range(number-1) : 
    print(' '*(y+2) + '★ '*(number-1-y))