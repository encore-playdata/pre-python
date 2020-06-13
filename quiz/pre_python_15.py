"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""
number = input("주민등록번호 : ")
number=number.split('-')[1]

if number[0] == '1' or number[0] == '3':
    print("남자")
elif number[0] == '2' or number[0] == '4':
    print("여자")