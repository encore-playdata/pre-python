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


def strChange(string):
    strList = list(string)
    for i, v in enumerate(strList):
        if not str(v).isspace():
            if ord("a") <= ord(str(v)) <= ord("z") or ord("A") <= ord(str(v)) <= ord("Z"):
                if str(v).isupper():
                    strList[i] = str(v).lower()
                else:
                    strList[i] = str(v).upper()
            else:
                return print("입력 형식이 잘못되었습니다.")
    return print("".join(strList))


string = input()

if string.isspace():
    print("공백만 입력할 수 없습니다.")
else:
    strChange(string)
