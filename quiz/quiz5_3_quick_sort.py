"""
퀵정렬
"""


def swap(lst, li, ri):
    lst[li], lst[ri] = lst[ri], lst[li]


def partition(lst, start, end):
    big = start

    for i in range(start, end):
        if lst[i] < lst[end]:
            swap(lst, big, i)
            big += 1

    swap(lst, big, end)
    return big


def quick_sort(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1

    # 정렬해야할 대상이 하나밖에 없거나 아예 없으면 base case.
    if end <= start:
        return

    pivot = partition(lst, start, end)
    quick_sort(lst, start, pivot - 1)
    quick_sort(lst, pivot + 1, end)

    return lst


print(quick_sort([6, 8, 3, 9, 10, 1, 2, 4, 7, 5]))
