list1 = [1,2,3,5,7,9]
list2 = [2,3,8,9]

list3 = []

for x in list1:
    if x not in list2:
        list3.append(x)
print(list3)