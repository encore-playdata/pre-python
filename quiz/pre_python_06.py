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
"""

n = int(input('숫자를 입력하세요 : '))
round = n*2+1
for i in range(round):
    if i < n:
        for j in range(n-i):
            print(' ', end='')
        for k in range(i):
            print('*', end='')
        print()

    if i == n:
        for l in range(n):
            print('*', end='')
        print()

    if i > n: # i > 6
        # n = 5
        # round = 11
        # i =
        # 6 7 8 9 10
        # 5 4 3 2 1
        for m in range(i-n):
            print(' ', end='')
        for o in range(round-i-1):
            print('*', end='')
        print()




