"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""

def Triangle(a,b):
    if a<0 or b<0:
        print('가로와 세로가 0보다 커야합니다.')
    else:
        return a*b//2
        

print(Triangle(10,20))