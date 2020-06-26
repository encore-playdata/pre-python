"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F

예시
<입력>
score : 88

<출력>
A

"""
score = int(input('score : '))
if 0 < score < 21:
  print('F')
elif 0 < score < 41:
  print('D')
elif 0 < score < 61:
  print('C')
elif 0 < score < 81:
  print('B')
elif 0 < score < 100:
  print('A')
else:
  print('0부터 100까지의 점수를 입력해 주세요.')
