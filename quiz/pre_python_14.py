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

def convert_alphabet_re():
    str_input = input()

    import re

    alpha_pattern = re.compile('[A-Za-z]')
    matched = re.match(alpha_pattern, str_input)

    if not matched:
        print("입력 형식이 잘못되었습니다.")
    elif str_input.islower():
        print(str_input.upper())
    else:
        print(str_input.lower())

convert_alphabet_re()



# def convert_alphabet1():
#     str_input = input()
#
#     if not isalpha(str_input):
#         print("입력 형식이 잘못되었습니다.")
#     elif str_input.islower():
#         print(str_input.upper())
#     else:
#         print(str_input.lower())

# convert_alphabet1()