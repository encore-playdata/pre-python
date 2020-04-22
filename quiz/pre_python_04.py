"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""
def Triangle(width, height):
    return int(width * height / 2)

width = int(input("삼각형의 가로의 길이를 입력하시오 : "))
height = int(input("삼각형의 높이를 입력하시오 : "))

print(Triangle(width,height))
