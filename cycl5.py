a = [1, 5, 9, 5, 8, 6, 3]
b = [1, 2, 3, 4, 5]

Res = [x for x in a if x in b]
print(Res)

result=list(set(a+b))
print(result)

a = [1,5,9,5,8,6,3]
b = [1,2,3,4,5]

c = a+b

print(c)
s = []
for x in c: