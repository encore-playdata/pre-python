"""
3. 재귀 호출을 이용한 <퀵 정렬> 문제

입력 예시)
list_ex3 = [6,8,3,9,10,1,2,4,7,5]

출력 결과)
[1,2,3,4,5,6,7,8,9,10]
"""

def quick_sort(arr):
    n = len(arr)
    if n <= 1: return arr

    # 먼저 리스트의 맨 마지막 값을 pivot 값으로 선택
    pivot = arr[-1]
    # pivot 값보다 작은 값, 동일한 값 그리고 큰 값을 담아둘 3개의 리스트를 생성
    less_arr, equal_arr, greater_arr = [], [], []

    # for문을 통해 각 값을 pivot과 비교 후에 해당하는 리스트에 추가
    # 그 다음 작은 값과 큰 값을 담고 있는 배열을 대상으로 퀵 정렬 함수를 재귀 호출
    # 마지막으로 재귀 호출의 결과를 다시 크기 순으로 합치기
    for i in arr:
        if i < pivot:
            less_arr.append(i)
        elif i > pivot:
            greater_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(less_arr) + quick_sort(equal_arr) + quick_sort(greater_arr)


list_ex3 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(list_ex3))