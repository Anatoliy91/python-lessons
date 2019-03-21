#def dect(dict1):

dict1 = ({'key1':{'k': [1,5,9,5,8,6,3]} , 'key2':{'k': [1,5,9,5,8,6,3, 5,9]}})
listik = []
for x in dict1.values():
    for y in x.values():
        print(y)
        if y.values in (y[0], y[1]):
                #in y(0) and y(1):
            listik.append(y)
            print(listik)
      #  return listik

#dect({'key1':{'k': [1,5,9,5,8,6,3]} , 'key2':{'k': [1,5,9,5,8,6,3, 5,9]}})