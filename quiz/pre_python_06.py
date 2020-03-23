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

print('숫자를 입력하세요 : ', end='')
num = int(input())
for i in range(num):
    for j in range(num - i - 2, -1, -1):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(num):
    for j in range(i+1):
        print(' ', end='')
    for j in range(num - i - 2, -1, -1):
        print('*', end='')

    print()
