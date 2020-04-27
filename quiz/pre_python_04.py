"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""
def Triangle(bomttom_len, height):
    return int(bomttom_len*height/2)

bomttom_len = int(input('삼각형 밑변 가로 길이를 입력하세요.'))
height = int(input('삼각형 높이를 입력하세요.'))

print(Triangle(bomttom_len, height))