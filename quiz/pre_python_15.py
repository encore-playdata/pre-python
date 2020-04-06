"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""

def gender_class():
    id_num = input("주민등록번호 : ").split('-')

    if id_num[1][0] in ['1', '3']:
        print("남자")
    else:
        print("여자")

gender_class()
