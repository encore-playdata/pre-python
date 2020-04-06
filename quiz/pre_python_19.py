"""19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']


예시
<입력>
print(list)

<출력>
['charlie', 'foxtrot']

 """

# 내가 작성한 답안
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
for i in range(9):
    list = a[i]
    if len(list) == 7:
        print(list)

# 실제 답안
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
list = []
for i in a:
    if len(i) == 7:
        list.append(i) # 리스트에서 알파벳 개수가 7개인 단어만 뽑아서 리스트에 하나씩 추가

print(list)