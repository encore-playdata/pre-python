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
maxNum = int(input("숫자를 입력하세요 : "))
for i in range(1, (maxNum*2)):
    for j in range(0, abs(maxNum - i)):
        print(' ', end='')
    if(i<=maxNum):
        for k in range(i, 0, -1):
            print('★', end='')
    else:
        for k in range(maxNum - abs(maxNum - i), 0, -1):
            print('★', end='')
    print('')