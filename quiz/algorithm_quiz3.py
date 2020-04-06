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
list=[4,3,2,1,8,7,5,10,11,16,21,6]

    #비교해서 뒤가 작았을 때 바꾼다 (앞이 더 클 때)

    #반복문 (# 0번째와 나머지를 모두 비교를 한다. 1바퀴) -> 가장 작은 것이 0번째에 온다.     -> 그다음 이거를 또 반복

    # 비교를 할 때, 예를 들어 list = [1,2,3,4]일때 (4개밖에 없으면) -> 총 n-1번만 비교를 해주면 됨
        # index가 0일때: 1,2,3
        # 1일때: 2,3 과비교
        # 2일때: 3하고만 비교하면 됨

def bubble_sort(arr):
    for front_index in range(0, len(arr)-1):

        for index in range(front_index+1, len(arr)):
            if arr[front_index] > arr[index]:
                temp = arr[front_index]
                arr[front_index] = arr[index]
                arr[index] = temp
    return arr

print(bubble_sort(list))
    # <출력> [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 16, 21]