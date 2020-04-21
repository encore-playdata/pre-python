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
def upperlower(words):
    import re
    # 영문자 외 문자 입력 시 메시지 출력
    if len(re.findall('[^a-z^A-Z]', words)) > 0:
        return print('입력 형식이 잘못되었습니다.')

    result = ''
    for word in words:
        result += (word.upper() if word.islower() else word.lower())    # 소문자 -> 대문자, 대문자 -> 소문자
    return print(result)