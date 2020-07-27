def fibonacci(n):
    list_n = []

    temp = 1
    for i in range(0, n-2):
        list_n.append(temp)
        if len(list_n) <= 1:
            temp += 1
        elif len(list_n) == 2:
            temp = list_n[0] + list_n[1]
        elif len(list_n) > 2:
            temp = list_n[i-1] + list_n[i] 
    return temp
    
    
print(fibonacci(10))