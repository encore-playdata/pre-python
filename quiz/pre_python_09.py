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

def eval_grade():
    grade = int(input('score : '))

    if grade > 80:
        return print('A')
    elif grade > 60:
        return print('B')
    elif grade > 40:
        return print('C')
    elif grade > 20:
        return print('D')
    else:
        return print('F')