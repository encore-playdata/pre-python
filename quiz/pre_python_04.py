"""
4.
삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.

예시
<입력>
print(Triangle(10,20))

<출력>
100
"""


def Triangle(width, height):   # 가로 width, 높이 height 인 삼각형 함수 선언
    area = width * height / 2  # 삼각형의 넓이 = 밑변 * 높이 / 2
    return area  # area 의 값을 리턴


print(Triangle(10, 20))     # 삼각형의 밑변과 높이의 값을 받아 넓이를 출력

