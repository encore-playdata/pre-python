def select_sort(lst):
    # len(lst) - 1
    # 선택정렬 특성상 마지막 남은 index 는 이미 정렬되어있다.
    for i in range(len(lst) - 1):
        min_index = i

        # i + 1
        # i는 이미 min_index 로써 선택되어 있으니 그 다음 인덱스부터 비교해나간다.
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


given_lst = [9, 4, 3, 1, 12]
print(select_sort(given_lst))
