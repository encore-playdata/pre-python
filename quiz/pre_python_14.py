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
from string import ascii_lowercase
from string import ascii_uppercase

smallLetter = list(ascii_lowercase)
bigLetter = list(ascii_uppercase)
bothLetter = smallLetter+bigLetter
str = input('영어 단어를 입력해 주세요 : ')

def exchangeFunc(str):
    newStr = []
    try:
        for i in range(len(str)):
            if str[i] not in bothLetter:
                raise ValueError
            elif str[i] in smallLetter:
                newStr.append(str[i].upper())
            else:
                newStr.append(str[i].lower())
        for i in range(len(newStr)):
            print(newStr[i], end="")
    except ValueError:
        print('입력 형식이 잘못되었습니다. ')
        str = input('영어 단어를 입력해 주세요 :')
        exchangeFunc(str)

exchangeFunc(str)

