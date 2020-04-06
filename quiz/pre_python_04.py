"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100
"""
def Trialgle(a,b):
    result = a*b*(1/2)
    return result

horizontal = int(input('삼각형의 가로의 길이를 입력해주세요.:'))
vertical = int(input('삼각형의 세로의 길이를 입력해주세요.:'))

print(Trialgle(horizontal,vertical))
