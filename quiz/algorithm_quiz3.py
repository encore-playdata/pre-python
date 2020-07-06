"""
3.
앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을
경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
list=[4,3,2,1,8,7,5,10,11,16,21,6]

<입력>
print(bubble_sort(list))

<출력>
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 16, 21]
"""


def bubble_sort(lst):
    # len(lst) - 1
    # 거품을 일으킬 때마다 뒤에서부터 정렬되는데 마지막에 남을 가장 첫번째 요소는 어차피 이미 정렬되어 있을 것이다.
    for i in range(len(lst) - 1):
        is_sorted = True

        # len(lst) - 1 - i
        # 2개씩 묶어서 전진해나가는데 그 중 j는 첫번째 요소이므로 마지막 요소 전까지만 전진한다.
        # 일으킨 거품이 한 차례씩 완료될 때마다 더 이상 검사가 필요없는 요소들이 뒤에서부터 하나씩 쌓여간다.
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_sorted = False

        # 거품이 올라가는 동안 한번도 교환이 일어나지 않았다면 이미 모두 정렬되어있단 뜻이다.
        if is_sorted:
            break

    return lst


given_lst = [4, 3, 2, 1, 8, 7, 5, 10, 11, 16, 21, 6]
print(bubble_sort(given_lst))
