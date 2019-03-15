x = 26

if x == 25:
    print("Yes, you are right")
else:
    print("No, you are wrong")



age = 7+1
if (age <= 4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teanjeajer")
else:
    print("You are old")

print("End")


all_cars = ['bmw', 'volksfagen', 'seat', 'skoda', 'lada', "mercedes", "ford"]
german_cars = ['bmw', 'volksfagen', "mercedes", "ford"]


if "lada" in all_cars:
    print("Yes lada is in the list")
else:
    print("not in the list lada")



all_cars = ['bmw', 'volksfagen', 'seat', 'skoda', 'lada', "mercedes", "ford"]
german_cars = ['bmw', 'volksfagen', "mercedes", "ford"]


for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is german car")
    else:
        print(xxxx + " not german car")
