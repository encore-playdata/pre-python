lst=[9,4,3,1,12]
tmp=[]
tmp.append(lst[0])
for i in range(1,len(lst)):
    tmp.append(lst[i])
    for j in range(i,0,-1):
        if tmp[j]<tmp[j-1]:
            tmp[j],tmp[j-1]=tmp[j-1],tmp[j]

    print(tmp)