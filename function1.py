#def napechatat_privetstvie(name):
#    """"print privetstvie"""
#    print("congratulation wish you " + name)


#def summa(x, y):
#    return x+y

#print("------------------")
#napechatat_privetstvie("Vasya")

#x = summa(33, 22)
#print(x)



def factorial(x):
    """"calculate factorial of number x"""
    result = 1
    max = x+1
    print("Max:" + str(max))
    for i in range(1, max):
        result = result * i
    return result


#for i in range(1,11):
# print(str(i)+ "!\t =" + str(factorial(i)))


#print(factorial(1))
print(factorial(5))
#print(factorial(10))
#print(factorial(20))
