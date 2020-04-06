"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""
print('<입력>')
id = input('주민등록번호 :')

print('<출력>')
id_split = id.split('-')
id_slice = int(id_split[1][0:1])
if id_slice == 1 or id_slice == 3:
    print("남자")
elif id_slice == 2 or id_slice == 4:
    print("여자")