enemy = {
            "location_x": 30,
            "location_y": 70,
            "color": "green",
            "health": 100,
            "name": "Mudila"

}

print(enemy)

print("location X =" + str(enemy["location_x"]))
print("location y =" + str(enemy["location_y"]))
print("His name is = " + enemy["name"])

enemy['rang'] = "admiral"
print(enemy)

del enemy['rang']
print(enemy)


enemy["location_x"] = enemy["location_x"] + 40
enemy["health"] = enemy["health"] - 30
if enemy["health"]<80:
    enemy["color"] = "yellow"

print(enemy)

print(enemy.keys())
print(enemy.values())