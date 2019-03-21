def uniq(list1, list2):
    #list1 = [1, 5, 9, 5, 8, 6, 3, 5, 6, 5, 6, 1, 6, 3, 5]
    #list2 = []
    a = 0

    for x in list1:
        if x not in list2 and x % 2 == 0:
            list2.append(x)


    for y in list2:
        a = a+y
    return a, list2


a, list2 = uniq(list2=[], list1=[1, 5, 9, 5, 8, 6, 3, 5, 6, 5, 6, 1, 6, 3, 5])
print(a)
print(list2)