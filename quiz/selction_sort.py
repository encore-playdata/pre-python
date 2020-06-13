lst = [9,4,3,1,12,7]

for i in range(len(lst)-1):
    min_number=i
    for j in range(i+1,len(lst)):
        if lst[min_number]>lst[j]:
            min_number=j

    lst[i],lst[min_number]=lst[min_number],lst[i]

#print(lst)