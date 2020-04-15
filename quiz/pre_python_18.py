"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py', 'hi.py', 'playdata.hwp', 'intro.jpg']

결과:
file = ['exit', 'hi', 'playdata', 'intro']

예시
<입력>
print(new_list)

<출력>
['exit', 'hi', 'playdata', 'intro']

"""

# 내가 작성한 답안
file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
for i in range(4):
    new_list = file[i].split(".")
    print(new_list[0])

# 실제 답안
file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
new_list=[]
for i in range(len(file)):
    a = file[i].split(".") # 먼저 리스트 file를 "."을 기준으로 분할
    new_list.append(a[0])  # 리스트 a는 "."을 기준으로 2개로 분할된 상태인데, 그 중에서 첫 번째 값을 append

print(new_list)