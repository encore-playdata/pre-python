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

input_english = input("대문자 혹은 소문자 영어를 입력하시오. : ")

if input_english.isupper() == True:
    print(input_english.lower())
elif input_english.islower() == True:
    print(input_english.upper())
else:
    print("입력 형식이 잘못되었습니다")
