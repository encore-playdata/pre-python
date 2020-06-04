"""19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']


예시
<입력>
print(list)

<출력>
['charlie', 'foxtrot']

 """

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']



list = []
for word in a: # a 리스트를 하나씩 포문에 넣는다.
    if len(word) == 7: # 이 때, a의 단어 글자수가 7개이면
        list.append(word) # 리스트 변수의 리스트에 삽입한다.


print(list) # 삽입한 것을 출력하라.
