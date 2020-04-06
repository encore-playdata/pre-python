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
star = int(input('숫자를 입력하세요 :'))
for i in range(1, star*2):
    if i <= star:
        s = '★'*i
        n = star
        print(s.center(n))
    else:
        s = '★'*(star*2-i)
        n = star
        print(s.center(n))
"""왜 삐뚤거리게 나오는지 모르겠어요......"""


