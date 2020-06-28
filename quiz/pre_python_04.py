"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""


def triangle(a, b):
    result = a * b * 1 / 2
    return result


w = float(input('삼각형의 가로는 몇 cm 입니까? : '))
h = float(input('삼각형의 높이는 몇 cm 입니까? : '))

print('삼각형의 넓이는 {} cm² 입니다.'.format(triangle(w, h)))
