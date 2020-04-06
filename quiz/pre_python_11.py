"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(x,y):
    xmax = max(x,y)
    xmin = min(x,y)
    for i in range(xmin):
        if xmax % (i+1) == 0 and xmin % (i+1) == 0 :
            result = i+1
    return result

print(gcd(12,6))