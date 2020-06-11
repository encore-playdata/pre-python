
list = [9, 4, 3, 1, 12]

def insert_sort(a):
        for i in range(1, len(a)):
            print(a)                     # 함수가 돌아가는 과정을 보고 싶다면
            for j in range(i):
              if a[i] < a[j]:
                    a.insert(j, a.pop(i))    # 0부터 자리를 잡고 리스트 j가 리스트 i보다 크면 j위치에 i값을 넣고 i는 지운다.
        return a

print(insert_sort(list))


