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
i = int(input("숫자를 입력하세요 : "))
star_number = 1
space = i - 1
while i >= star_number :
    print((" " * space) + ("★" * star_number))
    star_number = star_number + 1
    space = space - 1
    if space == 0:
        while i > space:
            print((" " * space) + ("★" * star_number))
            star_number = star_number - 1
            space = space + 1
        break

# 하긴 했는데 코드가 오래걸리고 복잡고 직관적이지 않음 .. 나중에 간단하게 고쳐보기
# continue, break 개념 다시 공부하기


