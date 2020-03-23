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

print('score : ', end='')
sc = int(input())
if 0 <= sc <= 20:
    print('F')
elif 21 <= sc <= 40:
    print('D')
elif 41 <= sc <= 60:
    print('c')
elif 61 <= sc <= 80:
    print('B')
elif 81 <= sc <= 100:
    print('A')
else:
    print('범위 초과')
