"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""
# 함수를 사용할 때는 행위가 필요할때? 그렇지만 행위 반복은 반복문이나 조건문으로도 충분히 가능
# 다양한 변수의 연산을 사용할때??

width = int(input("삼각형의 가로를 입력해 주세요 : "))
height = int(input("삼각형의 높이를 입력해 주세요 : "))

def Triangle(width, height):
    return width * height

print(Triangle(width, height))
