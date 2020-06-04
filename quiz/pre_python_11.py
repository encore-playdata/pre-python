"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(a, b):
    s1 =[]
    for i in range(1, a+1):
        if a % i == 0:
            s1.append(i)     # s1은 a의 약수

    s2=[]
    for j in range (1, b+1):
        if b % j == 0:
            s2.append(j)     # s2는 b의 약수

    s3=[]
    for k in s1:
        if k in s2:
            s3.append(k)

    return(s3[-1])      # s3은 공약수, 출력은 리스트 마지막에 위치한 최대공약수, -1사용.


print(gcd(10, 25))
