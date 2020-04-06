"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""

RRN = input('주민등록번호 : ')

splited = RRN.split('-')

seventh_digit = splited[1][0:1]

if seventh_digit == '9' or seventh_digit == '1' or seventh_digit == '3':
    print('남자')
elif seventh_digit == '0' or seventh_digit == '2' or seventh_digit == '4':
    print('여자')