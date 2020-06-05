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

def checkEngAlpha(Alphabets):
    for i in range(len(Alphabets)):
        chara = Alphabets[i]
        if 'a' <= chara <= 'z' or 'A' <= chara <= 'Z':
            if "".join(Alphabets).isupper(): return "".join(Alphabets).lower()
            else: return "".join(Alphabets).upper()
        else: return "입력 형식이 잘못되었습니다."

Alphabets = list(input('<입력>'))

print(checkEngAlpha(Alphabets))