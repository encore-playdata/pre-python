"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def divisor(x):
	z = []
	for i in range(1,int(x/2)+1):
    		if x%i == 0:
        			z.append(i)
	z.append(x)
	return z

def max(arg1):
	max=0
	for i in arg1:
    		if max<i:
        			max=i
	return max

def intersection(arg1,arg2):
	z=[]
	for i in arg1:
    		if i in arg2:
        			z.append(i)
	z.sort()
	return z

def gcd(arg1,arg2):
	d1=divisor(arg1)
	d2=divisor(arg2)
	result=intersection(d1,d2)
	return max(result)
print(gcd(12,6))