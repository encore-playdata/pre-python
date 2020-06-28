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
n = int(input('숫자를 입력하세요. : '))
for i in range(n * 2 - 1):
    if(i < n):
        for j in range(i, n-1):
            print(end=' ')
        for k in range(i+1):
            print('★', end='')
    else:
        for b in range(n, i+1):
            print(end=' ')
        for a in range(i, n *2 -1):
            print('★', end='')
    print()

