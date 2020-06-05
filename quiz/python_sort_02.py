def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j + 1] < list[j]:
                list[j], list[j + 1] = list[j + 1], list[j]

list = [9, 4, 3, 1, 12]

bubbleSort(list)
print(list)