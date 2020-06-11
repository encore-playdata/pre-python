"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']

예시
<입력>
print(new_list)

<출력>
['exit', 'hi', 'playdata', 'intro']

"""
file = ['exit.py', 'hi.py', 'playdata.hwp', 'intro.jpg']

import os

# new_list = [os.path.splitext(x)[0] for x in file] 방법이 두 개다.

new_list = []
for x in file:
    new_list.append(os.path.splitext(x)[0]) # 새로운 변수를 만들어 확장자를 없앤 파일명을 넣어준다.
print(new_list)

