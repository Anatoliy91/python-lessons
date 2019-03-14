enemy = {
            "location_x": 30,
            "location_y": 70,
            "color": "green",
            "health": 100,
            "name": "Mudila",
            "awards": {"za stalina", "za lenina"},
            "image": {"image1","image2","image3"}

}


all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())
    print(all_enemies)

for x2 in all_enemies:
    print(x2)

all_enemies[5]["health"] = 30
all_enemies[6]["name"] = "Kozel"
for ene in all_enemies:
    print(ene)


