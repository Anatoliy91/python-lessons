Listik =[{' key1' :[1, 2,3,6],' key2' :[22, 58,88]}, {' key1' :[1, 2,3,6],' key2' :[22, 58,88]}]

for a in Listik:
    for b in a.values():
        for c in b(1):
            if c % 2 ==0:
                print(c)