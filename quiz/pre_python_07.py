"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오


<출력>
 45
"""

Num_sum = 0

for n in range(1, 101):
    Num_sum = Num_sum + n
    if Num_sum > 1000:
        print(n)
        break