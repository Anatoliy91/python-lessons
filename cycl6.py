def cycle6(list1, list2):

    list3 = []

    for x in list1:
        if x not in list2:
            list3.append(x)
    print(list3)

cycle6([2,4,5,6,8,9,7,5], [2,3,4,5,6,7,8,95])
