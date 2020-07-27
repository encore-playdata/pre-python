def merge_sort(list):
    g1 = list[:len(list)//2]
    g2 = list[len(g1):]
    g1.sort()
    g2.sort()
    return merge(g1, g2)

def merge(g1, g2):
    result = []
    i = 0
    while True:
        if g1 == [] :
            for i in range(len(g2)):
                result.append(g2[i])
            while True:
                if 0 <= len(g2):
                    del g2[0]
                elif g2 == []:
                    print(result)
                    return False
        if g2 == [] :
            for i in range(len(g1)):
                result.append(g1[i])
            while True:
                if 0 < len(g1):
                    del g1[0]
                elif g1 == []:
                    print(result)
                    return False
        elif g1[i] >= g2[i]:
            result.append(g2[i])
            del g2[i]
        elif g1[i] <= g2[i]:
            result.append(g1[i])
            del g1[i]

list = [6,8,3,9,10,1,2,4,7,5]
merge_sort(list)