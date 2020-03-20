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
# 알파벳 범위 설정 확인 다른 범위가 있는지 생각해보기

word = input()
def up_word(word):
    return word.upper()

if word == int or word == float:
    print("입력 형식이 잘못되었습니다.")
elif word >= 'a' and word <= 'z':
    print(up_word(word))
else:
    print("입력 형식이 잘못되었습니다.")