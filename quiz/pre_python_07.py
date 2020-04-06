"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오


<출력>
 45
"""
num_1_to_100 = 1
sum_result = 0

for number in range(1, 101):
    sum_result += number
    if sum_result < 1000:
        num_1_to_100 += 1
        continue
    print(num_1_to_100)
    break
