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

n = input('score : ')

if int(n) > 80 and int(n) <= 100:
    print('A')
elif int(n) > 60 and int(n) <= 80:
    print('B')
elif int(n) > 40 and int(n) <= 60:
    print('C')
elif int(n) > 20 and int(n) <= 40:
    print('D')
elif int(n) >= 0 and int(n) <= 20:
    print('F')