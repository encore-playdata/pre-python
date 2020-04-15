"""
2. 재귀 호출을 이용한 <병합 정렬> 문제

입력 예시)
list_ex2 = [6,8,3,9,10,1,2,4,7,5]

출력 결과)
[1,2,3,4,5,6,7,8,9,10]
"""

def merge_sort(arr):
    n = len(arr)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n <= 1: return arr

    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    half = n // 2
    g1 = arr[:half]
    g2 = arr[half:]
    merge_sort(g1)
    merge_sort(g2)

    # 두 그룹을 합치는 과정(병합)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            arr[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            arr[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1):
        arr[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2):
        arr[ia] = g2[i2]
        i2 += 1
        ia += 1


list_ex2 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(list_ex2)
print(list_ex2)