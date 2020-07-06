"""
2.
첫 번째 숫자를 두 번째 숫자부터 마지막 숫자까지 차례대로 비교하여
가장 작은 값을 찾아 첫 번째에 놓고,  두번째 숫자를 세 번째 숫자부터
마지막 숫자까지 차례대로 비교하여그 중 가장 작은 값을 찾아
두 번째 위치에 놓는 과정을 반복하며 정렬하는것을 선택정렬이라고 합니다.
주어진 리스트를 선택정렬함수(select_sort)를 생성하여 오름차순으로 정렬하시오
list=[6,2,3,7,8,10,21,1]

<입력>
print(select_sort(list))

<출력>
[1, 2, 3, 6, 7, 8, 10, 21]

"""


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


given_lst = [6, 2, 3, 7, 8, 10, 21, 1]
print(select_sort(given_lst))
