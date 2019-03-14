cities = ["kiev", "moscow", "kiev1", "lonoon", "new jersey", "New York"]
enter_name = input("Enter your name\n")

while True:
    enter_city = input("Enter city, " + enter_name + "\n")

    last_char = enter_city[-1]
    print("Next city will be on char " + last_char)
    city_found = False

    for i in range(cities.__len__()):
        first_char = cities[i][0]
        if first_char == last_char:
            print(cities[i])
            city_found = True
            del cities[i]
            break

    if city_found == False:
        print("Ya proigral")
        break