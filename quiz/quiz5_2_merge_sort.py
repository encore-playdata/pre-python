"""
병합정렬
"""


def merge(left, right):
    lst = []
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            lst.append(left[li])
            li += 1
        else:
            lst.append(right[ri])
            ri += 1

    if li == len(left):
        lst += right[ri:]
    else:
        lst += left[li:]

    return lst


def merge_sort(lst):
    mid = len(lst) // 2
    if mid == 0:
        return lst

    left = lst[:mid]
    right = lst[mid:]

    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([6, 8, 3, 9, 10, 1, 2, 4, 7, 5]))
