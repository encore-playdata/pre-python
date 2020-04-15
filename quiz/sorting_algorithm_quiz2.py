'''
2. <버블 정렬> 문제
문제)
주어진 리스트를 오름차순으로 정렬하시오.
[7, 4, 5, 1, 3]

결과)
[1, 3, 4, 5, 7]
'''

arr2 = [7, 4, 5, 1, 3]
n = len(arr2)

for i in range(0, n):
    for j in range(n - 1, i, -1):
        if arr2[j - 1] > arr2[j]:
            arr2[j - 1], arr2[j] = arr2[j], arr2[j - 1]

print(arr2)