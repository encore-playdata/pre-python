def selectionSort(list):
    for i in range(len(list) - 1):
        MinIndex = i
        for j in range(i + 1, len(list) - 1):
            if list[j] < list[MinIndex]:
                MinIndex = j
        list[i], list[MinIndex] = list[MinIndex], list[i]

list = [9, 4, 3, 1, 12]

selectionSort(list)
print(list)