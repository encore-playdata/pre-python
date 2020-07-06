"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""

# rrn (Resident Registration Number)
rrn = input("주민등록번호 : ")

second_numbers = rrn.split('-')[1]
gender_info = int(second_numbers[:1])

if gender_info % 2 == 0:
    print('여자')
else:
    print('남자')
