

list = [7,4,5,1,3]

def bubble_sort(a):
        for i in range(0, len(a)):

            for j in range(len(a)-1, i, -1):
                if a[j-1] > a[j]:
                    a[j-1], a[j] = a[j], a[j-1]
        return a

print(bubble_sort(list))