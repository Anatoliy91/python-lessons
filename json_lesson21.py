import json

filename = "user_settings.txt"
myfile = open(filename, mode = "w", encoding="Latin-1")

player1 ={
    'PlayerName' : "Donald Trump",
    'Score' : "345",
    'Awards' : ["OR", "NY", "NW"]
}

player2 = {
'PlayerName' : "Killari Clintonp",
    'Score' : "380",
    'Awards' : ["VA", "VT", "NY"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)


#-----------Save by json-------------------


json.dump(myplayers, myfile)

myfile.close()


#===============Load by json===========

myfile = open(filename, mode="r")
json_data = json.load(myfile)
print(json_data)

for user in json_data:
    print("player name is" + str(user['PlayerName']))
    print("player score " + str(user['Score']))
    print("Player awards" + str(user["Awards"][0]))
    print("Player awards" + str(user["Awards"][1]))
    print("Player awards" + str(user["Awards"][2]))