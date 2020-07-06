def insertion_sort(lst):
    # range(1, len(lst))
    # 0번방은 이미 정렬되어있는 1개짜리 리스트로 볼 수 있기 때문에
    # 실질적으로는 1번방부터 마지막 방에 있는 값들까지만 삽입할 장소를 찾아준다.
    for i in range(1, len(lst)):
        # 이미 정렬되어 있는 리스트에서 i번방 값을 삽입할 위치를 찾는다.
        for j in range(i):
            # 정렬되어 있는 리스트 중 i번방 값보다 더 큰 값이 있다면 그 앞 자리로 삽입한다.
            if lst[i] < lst[j]:
                temp = lst[i]
                del lst[i]
                lst.insert(j, temp)
                break

    return lst


given_lst = [9, 4, 3, 1, 12]
print(insertion_sort(given_lst))
