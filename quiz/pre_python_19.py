"""
19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']


예시
<입력>
print(list)

<출력>
['charlie', 'foxtrot']
"""


a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']  # 기존 파일 리스트
list = []   # 추가로 넣을 리스트

for i in a:
    if len(i) == 7:     # len 리스트의 크기 함수
        list.append(i)  # list 리스트에 7자인 단어 추가

print(list)     # list 리스트 출력
