num = input("Enter your name")

if int(num) > 0:
    if int(num)> 10:
        print("entered >10")
    else:
        print('entered <10 and >0')
elif int(num) == -10:
    print("entered=10")
elif int(num) == -15:
    print("entered=15")
elif int(num) <-20:
    print("entered<20")



else:
    print("vu vveli <0 and > -10")


name = input()
A = 'Yes' if name != "Test" else 'No'
print(A)