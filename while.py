i = 0
while i <= 10:
    print(i)
    i += 2

b = 1000
while b >100:
    print(b)
    b /=2

for j in 'hello world':
    if j == 'a':
        break
    print(j*2, end = '')
else:
    print("letter a isn't in world")