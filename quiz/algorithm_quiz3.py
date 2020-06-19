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

def bublle_sort(l):
    loop_count = 0
    print(l)
    s_flg = False # flag for sawp
    for _ in range(len(l) - 1):
        # 모든 인덱스에 대해 실행
        for j in range(len(l) - 1):
            # 내부 루프, 비교 스왑 -> 비교 스왑, 모든 원소 확인할 때까지
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j + 1], l[j]
                s_flg = True
        if s_flg == False: # when swap does not occur, escape
            break
    print(l, 'loop count : ', loop_count)


def main():
    bublle_sort([4,3,2,1,8,7,100,21,1500,1300,1200,5,10,11,16,21,6])


main()