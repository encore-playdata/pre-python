"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오.

예시
<입력>
EAST
<출력>
east

<입력>
hello
<출력>
HELLO

<입력>
안녕
<출력>
입력 형식이 잘못되었습니다.

"""
"""import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789"""

import string
english = string.ascii_letters
alpha = list(english)
print(alpha)
str = input('영어를 입력하세요.')
print(alpha[0] in str )

str = input('영어를 입력하세요.')
for i in range(len(alpha)):
    if alpha[i] in str:
        if str.islower():
            print(str.upper())
            break
        else:
            print(str.lower())
            break
    else:
        print('입력 형식이 잘못되었습니다')
"추가 수정 필요"

