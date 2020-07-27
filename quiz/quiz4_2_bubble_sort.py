def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
list = [7,4,5,1,3]
print(bubble_sort(list))
