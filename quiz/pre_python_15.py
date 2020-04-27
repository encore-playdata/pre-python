"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""
str = input('주민등록번호 : ')
str_split = str.split('-')
str_list = list(str_split[1])

if str_list[0] == '3' or str_list[0] == '1':
    print('남자')
elif str_list[0] == '2' or str_list[0] == '4':
    print('여자')
else:
    print('잘못된 값 입력됨')