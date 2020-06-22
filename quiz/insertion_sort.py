"""
########### 삽입 정렬 #############

"""

def insertion_sort(arr):
    n = len(arr)

    for end in range(1, n):
        for j in range(end, 0, -1):
            if arr[j-1] >arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j-1]
    return arr

arr = [9, 4, 3, 1, 12]
print(insertion_sort(arr))