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
# def selection_sort(list):
  #    if list != []:
   #       x = min(list)
    #      list.remove(x)
     #     return[x] + selection_sort(list)
      # else:
        #  return[]






def select_sort(a):


    for i in range(len(a)): # 리스트의 크기-1만큼 반복, 그럼 마지막 수는 어떻게 비교?

        for j in range(i+1, len(a)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
            if a[i] > a[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면 / 6하고 2~21까지 비교교하는데 6보다 작은 건 다 걸리는 거 아닌가? 어떻게 최소값 하나만 나오게 하는지?
                a[i] , a[j]  = a[j], a[i] # swap 해주기
    return a


list = [6,2,3,7,8,10,21,1]

print(select_sort(list))
# 정렬 후 리스트


