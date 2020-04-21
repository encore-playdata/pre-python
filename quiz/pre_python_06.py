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
def print_star():
    n = int(input('숫자를 입력하세요 : '))

    for num in range(1, n+1):
        print('{:>{}}'.format('*'*num, n))
    for num in range(n-1, 0, -1):
        print('{:>{}}'.format('*'*num, n))
    return