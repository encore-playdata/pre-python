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
'''
number = int(input('숫자를 입력하세요. : '))

for i in range(number):
    for j in range(number-i):
        print(' ', end='')
    for k in range(j):
        print('★', end='')
    print()
'''
'''
for j in range(number, 1, -1):
    print('★', end='')
'''
'''
for j in range(6):
    print(j)
for j in range(6, 1, -1):
    print(j)
'''