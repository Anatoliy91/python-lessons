
cars = ['bmw', 'volksfagen', 'seat', 'skoda', 'lada']

for car in cars:
    print(car.upper())


for x in range(1, 6):
    print(x)



mynumber_list = list(range(0, 10))
print(mynumber_list)

print("___________________________________________")

for x in mynumber_list:
    x = x * 2
    print(x)


mynumber_list.sort(reverse=False)
print(mynumber_list)

print("Max number in list " + str(max(mynumber_list)))
print("Min number in list " + str(min(mynumber_list)))
print("Sum of list " + str(sum(mynumber_list)))


print("___________________________________________")


cars = ['bmw', 'volksfagen', 'seat', 'skoda', 'lada']


mycars = cars[1:4]
print(mycars)

mycars = cars[:3]
print(mycars)

mycars = cars[-3:]
print(mycars)


cars = ['bmw', 'volksfagen', 'seat', 'skoda', 'lada']
mycars = cars[:]

cars.remove("bmw")    # удалить элемент массива


print(mycars)
print(cars)


mycars = cars[::-1]  # перевернуть массив
print(mycars)




rod = ["papa", "mama", "marina", "brat1", "brat2"]

print(rod[::-1])

rod.sort()
print(rod)

rod.sort(reverse=True)
print(rod)

print(rod[1:3])


