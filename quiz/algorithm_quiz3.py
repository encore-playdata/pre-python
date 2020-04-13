'''
3.
앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을
경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
list=[4,3,2,1,8,7,5,10,11,16,21,6]

<입력>
print(bubble_sort(list))

<출력>
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 16, 21]
'''

# len(arr)가 4라면
# 바깥 루프는 3번 돌아야 하므로
# range()는 0, 1, 2까지 즉 range(3)이 되야 하므로
# range(len(arr)-1)이 되어야 한다.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # 안쪽 루프는 1번당 3 -> 2 -> 1
        # 즉, range(4 - 0 - 1) ->
        # range(4 - 1 - 1) ->
        # range(4 - 2 - 1)
        # range(n - i - 1)
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # 만약 앞에 있는 값이 크다면 두 개를 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


list_ex3 = [4, 3, 2, 1, 8, 7, 5, 10, 11, 16, 21, 6]
bubble_sort(list_ex3)
print(list_ex3)