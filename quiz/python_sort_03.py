def insertionSort(list):
    for i in range(1, len(list)):
        while i > 0 and list[i] < list[i - 1]:
            list[i], list[i - 1] = list[i - 1], list[i]
            i -= 1

list = [9, 4, 3, 1, 12]

insertionSort(list)
print(list)