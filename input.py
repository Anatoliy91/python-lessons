#name = input("Please enter your name: ")
#print("Privet " + name)

#num1 = input("Enter x: ")
#num2 = input("Enter y: ")

#summa =int(num1) + int(num2)
#print(summa)
message = ""

#while True:
#    message = input("enter password")
#    if message == "sekret":
#        break
#    print(message + "password not correct")

#print("Password was:" + message)


mylist = []
msg = ""

while msg != 'stop'.upper():
    msg = input("Enter new iten, and Stop to finish")
    mylist.append(msg)

print(mylist)