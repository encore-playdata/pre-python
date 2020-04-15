"""
1. <선택 정렬> 문제
문제)
[9, 4, 3, 1, 12]을 오름차순으로 정렬하시오.

결과)
[1, 3, 4, 9, 12]
"""

arr1 = [9, 4, 3, 1, 12]
n = len(arr1)

for i in range(0, n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if arr1[j] < arr1[min_idx]:
            min_idx = j
    arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i]

print(arr1)