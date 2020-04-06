'''
3.
앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을
경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
list=[4,3,2,1,8,7,5,10,11,16,21,6]

<입력>
print(bubble_sort(list))

<출력>
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 16, 21]'''

list=[4,3,2,1,8,7,5,10,11,16,21,6]
'''
#부호가 틀렸고 두번째 range 첫번째 변수가 틀렸다.  버블정렬은 처음부터 다시 버블정렬을 하는 것이므로 i가 아니라 0이 맞음. 
def bubble_sort(list):
    length = len(list)
    for i in range(0, length-1):
        for j in range(i, length-1):
            if list[j] < list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list)
    return list
'''
'''
#0부터 시작하는 거라면 range를 좀 더 줄일 수 있다. 
def bubble_sort(list):
    length = len(list)
    for i in range(0, length-1):
        for j in range(0, length-1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
'''

def bubble_sort(list):
    length = len(list)
    for i in range(length-1):
        for j in range(length-1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubble_sort(list))

