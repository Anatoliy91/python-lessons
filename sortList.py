def listsort():
list1 = input('Enter list')
print("spisok" + list1)
for i in list1:
    if list1[i][0]>list1[i][-1]:
        print(list1[i])
