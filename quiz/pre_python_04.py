"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""
def Triangle(base, height):
    area = base * height / 2
    return area

print(Triangle(10, 20))