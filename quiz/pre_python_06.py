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
space = " "
star = "*"

for i in range(round):
    if i < n: print(space*(n-i) + star*i)
    if i >= n: print(space * (i - n) + star * (round - i - 1))
# i > 6
# n = 5
# round = 11
# i =
# 6 7 8 9 10
# 5 4 3 2 1






