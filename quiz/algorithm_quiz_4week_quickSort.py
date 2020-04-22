'''
    list = [6,8,3,9,10,1,2,4,7,5]
    
    우선 리스트에서 기준값을 하나 정해야 합니다.
    편의상 리스트의 맨 마지막 값을 기준값으로 정하였습니다.
    
    list = [6,8,3,9,10,1,2,4,7,5]의 기준 값 : 5
    
    기준값보다 작은 값을 저장할 리스트로 g1 , 큰 값을 저장할 리스트로 g2를 만듭니다.
    g1 : [ ]
    g2 : [ ]
    
    리스트에 있는 자료들을 기준 값인 5와 차례로 비교하여 5보다 작은 값은 g1, 5보다 큰 값은
    g2에 넣습니다. 예를 들어 6은 5보다 크므로 g2에 넣고, 그 다음 값인 8도 5보다 크므로 g1에 넣고
    3은 5보다 작으므로 g1에 넣습니다.
    g1 : [3,1,2,4]
    g2 : [6,8,9,10,7]
    
    재귀호출을 이용하여 g1을 정렬합니다. 함수 안에서 퀵 정렬을 재귀 호출하면서 문제를 풀어 정렬합니다.
    g1 : [1,2,3,4]
    
    재귀호출를 이용하여 g2를 정렬합니다. 마찬가지로 퀵 정렬로 문제를 풀어 정렬합니다.
    g2 : [6,7,8,9,10]
    
    이제 g1에는 '기준보다 작은 값들'이 정렬되어 있고, g2에는 '기준보다 큰 값들'이 정렬되어 있습니다.
    따라서 g1, 기준값 , g2를 순서대로 이어 붙이면 정렬이 완료됩니다.
    
    [1,2,3,4] + [5] + [6,7,8,9,10]
    
    결과
    [1,2,3,4,5,6,7,8,9,10]
    
    '''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

list = [6,8,3,9,10,1,2,4,7,5]

print(quick_sort(list))
