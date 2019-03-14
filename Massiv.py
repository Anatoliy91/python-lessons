cities = ['New York', 'moscow', 'Kiev', 'simferopol', 'Toronto']
print(cities)
print(len(cities))
print(cities[0])
print(cities[-2])
print(cities[-2].upper())
print(cities[-2].title())

cities[2] = 'Tula'

print(cities)

cities.append('kursk')
print(cities)

cities.insert(0, 'yalta')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop()
print("deleted city " + deleted_city)


print(cities)
cities.reverse()
print(cities)

















