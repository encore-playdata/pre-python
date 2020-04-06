"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""


def Triangle(x, y):
    return x * y / 2


x = input("가로 : ")
y = input("세로 : ")
print(Triangle(int(x), int(y)))
