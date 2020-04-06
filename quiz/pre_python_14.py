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
x= input('영어를 입력하세요 :')

print('<출력>')
if x.islower():
    print(x.upper())
elif x.isupper():
    print(x.lower())
else:
    print('입력 형식이 잘못되었습니다.')