"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a,b):
    if a>b:
        x=a
        y=b
    else:
        x=b
        y=a
    for i in range(y):
        if (x%(y-i)==0) & (y%(y-i)==0):
            break
    return y-i
print(gcd(63,56))