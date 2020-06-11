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
a = int(input('숫자를 입력하세요 :'))

if isinstance(a, int):
    for b in range(1, a+1):
        c = a - b
        d = c * ' '
        e = b * '★'
        print('{}{}'.format(d, e))
    for b in range(a, 0, -1):
        c = b - 1
        d = (a-c) * ' '
        e = c * '★'
        print('{}{}'.format(d, e))