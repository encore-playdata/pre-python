"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
# 약수의 갯수를 일단 구해야겠지. 일단 그럼 변하는 수는 두개
def highestFactor(numX,numY):
    if numX > numY:
        x = numY
    else:
        x = numX
    while x > 1:
        if numX % x == 0 and numY % x == 0:
            break
        x -= 1
    print(x)

highestFactor(16,8)