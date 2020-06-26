"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""
regNumbers = input()
regNumber = regNumbers.split('-')
regNumber2 = regNumber[1:]
regNumber3 = ''.join(regNumber2)
if regNumber3[0] == '1':
  print('남자')
elif regNumber3[0] == '3':
  print('남자')
else:
  print('여자')