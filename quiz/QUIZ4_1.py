

list = [9, 4, 3, 1, 12]

def select_sort(a):

        for i in range(len(a)):
        print a
            for j in range(i+1, len(a)):
                print(a)
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
        return a


print(select_sort(list))
