"""
3. <삽입 정렬> 문제
문제)
[9, 4, 3, 1, 12]을 오름차순으로 정렬하시오

결과)
[1, 3, 4, 9, 12]
"""

arr3 = [9, 4, 3, 1, 12]
n = len(arr3)

# 새롭게 추가된 값보다 작은 숫자를 만나는 최초의 순간까지만 내부 반복문을 수행
for end in range(1, n):
    i = end
    while i > 0 and arr3[i - 1] > arr3[i]:
        arr3[i - 1], arr3[i] = arr3[i], arr3[i - 1]
        i -= 1

print(arr3)