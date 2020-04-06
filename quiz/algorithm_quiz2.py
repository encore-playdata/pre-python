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

def select_sort(list):
    for i in range(len(list)):
        min_value = list[i]
        for j in range(i, len(list)):
            if list[j] < min_value:
                min_value = list[j]
        list.insert(i, list.pop(list.index(min_value)))
    return list

list=[6,2,3,7,8,10,21,1]
print(select_sort(list))