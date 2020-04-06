"""
19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

예시
<입력>
print(list)

<출력>
['charlie', 'foxtrot']
 """
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
a0 = list(a[0])
a1 = list(a[1])
a2 = list(a[2])
a3 = list(a[3])
a4 = list(a[4])
a5 = list(a[5])
a6 = list(a[6])
a7 = list(a[7])
a8 = list(a[8])

def sevenWords(a):
    if len(a) >= 7:
        print("".join(a),end=" ")

print(sevenWords(a0),sevenWords(a1),sevenWords(a2),sevenWords(a3),sevenWords(a4),sevenWords(a5),sevenWords(a6),sevenWords(a7),sevenWords(a8))