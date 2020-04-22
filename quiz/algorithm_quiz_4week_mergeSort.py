''' 
list = [6,8,3,9,10,1,2,4,7,5]
    
우선 리스트를 반으로 나누어야 합나디.
g1 : [6,8,3,9,10]
g2 : [1,2,4,7,5]

두 그룹을 각각 정렬합니다.(여기서 재귀호출을 이용해야 합니다!)
g1 : [3, 6, 8, 9, 10]
g2 : [1, 2, 4, 5, 7]

이제 두 그룹을 합쳐서 다시 한 그룹으로 만들겠습니다(병합)
g1 의 0번 인덱스3과 g2의 0번 인덱스1을 비교하여 더 작은 1을 결과 리스트에 넣습니다.
g1 : [3, 6, 8, 9, 10]
g2 : [2, 4, 5, 7]
result : [1]

두 그룹의 첫번째 값들을 비교하여 작은 값을 빼내 결과 리스트에 넣는 과정을 반복합니다.
이번에는 g2의 2가 빠져나오게 됩니다.
g1 : [3, 6, 8, 9, 10]
g2 : [2, 4, 5, 7]
result : [1,2]

이번엔 g1의 3이 뽑혀 정렬이 됩니다.
g1 : [6, 8, 9, 10]
g2 : [2, 4, 5, 7]
result : [1,2,3]

이과정을 반복하다 보면 한 그룹의 자료가 다 빠져 나가게 됩니다.
g1 : [8, 9, 10]
g2 : [ ]
result : [1,2,3,4,5,6,7]

g2엔 더이상 자료가 없으므로 더이상 비교할 필요 없이 g1의 자료값들을 
전부 result 로 옮기면 정렬이 끝나게 됩니다.
g1 : [ ]
g2 : [ ]
result : [1,2,3,4,5,6,7,8,9,10]

결과
[1,2,3,4,5,6,7,8,9,10]

'''

list = [6,8,3,9,10,1,2,4,7,5]

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

print(merge_sort(list))