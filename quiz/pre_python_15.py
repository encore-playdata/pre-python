"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""

def checkSex(IDNs):
    Factors = IDNs.split()
    Number = list(Factors[2])
    if int(Number[7]) % 2 == 0: return '여자'
    else: return '남자'

IDNs = input('<입력> 주민등록번호 : 000000-0000000 ')

print(checkSex(IDNs))