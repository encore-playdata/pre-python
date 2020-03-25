'''
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

'''

list=[6,2,3,7,8,10,21,1]

'''#이건 너무 불필요하게 어렵게 생각한 것. 반복문의 인자를 원소의 인덱스라 아니라 원소 그 자체로 하려고 했다. 
def select_sort(list):
    for i in list:
        for j in range(list.index(list[i+1]), len(list)):
            if list[j] > 
'''


'''
#원소의 인덱스를 활용하는 방법을 썼다. 
#여기에서 더 줄일 수 있다. 처음 반복문에서 리스트 끝항목까지 갈 필요는 없음. 
#스왑과정에서 min변수를 쓰지 않는데 불필요하게 min을 선언해서 활용.
 
def select_sort(list):
    for i in range(0, len(list)):
        min = list[i]
        minIndex = i
        for j in range(i+1, len(list)):
            if min > list[j]:
                min = list[j]
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list
'''


def select_sort(list):
    # 여기에 써야 len함수를 한번만 쓸 수 있다. 그리고 첫번째 반복문을 len(list)-1번만 반복함.
    length = len(list)
    for i in range(0, length-1):
        minIndex = i
        for j in range(i+1, length):
            if list[minIndex] > list[j]:
                # 최소인덱스를 갱신하고 최소인덱스를 활용하는 방법.
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list

print(select_sort(list))