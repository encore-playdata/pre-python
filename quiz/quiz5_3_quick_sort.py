def quick_sort(list):
    pivot = []
    pivot.append(list[-1])
    g1 = []
    g2 = []
    for i in range(0, len(list)):
        if list[i] < pivot[0] :
            g1.append(list[i])
        elif list[i] > pivot[0] :
            g2.append(list[i])
    result = quick_glue(sort(g1), pivot, sort(g2))
    return result
    


def sort(list):
    list.sort()
    return list

def quick_glue(g1, pivot, g2):
    list = []
    list = g1 + pivot + g2
    return list

list = [6,8,3,9,10,1,2,4,7,5]
print(quick_sort(list))