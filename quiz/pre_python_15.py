"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""

'''
ssNumber = input("주민등록번호를 입력해 주세요 :")
ssNumber=ssNumber.split("-")
ssNumber=ssNumber[1]
ssNumber=list(ssNumber)

if ssNumber[0] in '1' or ssNumber[0] in '3':
    print ('남자')
elif ssNumber[0] in '2' or ssNumber[0] in '4':
    print('여자')
else:
    print('잘못 입력 하셨습니다.')
'''
ssNumber = input("주민등록번호를 입력해 주세요 :")
if ssNumber[7] in '1' or ssNumber[7] in '3':
    print ('남자')
elif ssNumber[7] in '2' or ssNumber[7] in '4':
    print('여자')
else:
    print('잘못 입력 하셨습니다.')