def even():
    default_list=list(range(1,11))
    print(default_list)
    l=[]

    for i in default_list:
        if (i%2==0):
            l.append(i)
    return l
        

print(even())


