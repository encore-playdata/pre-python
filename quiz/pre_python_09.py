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

# 내가 작성한 답안(더 쉽게 코딩할 수 있었는데..)
score = int(input("score : "))
if score >= 81 and score <= 100:
    print("A")
elif score >= 61 and score <= 80:
    print("B")
elif score >= 41 and score <= 60:
    print("C")
elif score >= 21 and score <= 40:
    print("D")
else:
    print("F")

# 실제 답안
score = int(input("score : "))
if score > 80:
    print("A")
elif score > 60:
    print("B")
elif score > 40:
    print("C")
elif score > 20:
    print("D")
else:
    print("F")
