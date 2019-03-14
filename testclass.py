class people():
    def __init__(self, fname, lname, height, weight):
        self.fname = fname
        self.lname = lname
        self.height = height
        self.weight = weight

    def showninfoaboutpeople(self):
        description = (self.fname + " " + self.lname + " " + str(self.height) + " " + "sm" + " " + str(self.weight) + " " + "sm")
        print(description)


class superpeople(people):
    def __init__(self, fname, lname, height, weight, age):
        super().__init__(fname, lname, height, weight)
        self.age = age

    def up_age(self):
        self.age = 10


mysuperpeople = superpeople("terkin", "vasiliiii", "30", "120", "10")
mysuperpeople.showninfoaboutpeople()
mysuperpeople.up_age()
mysuperpeople.showninfoaboutpeople()


mypeople = people("vasya", "petrovich", "120", "160")
mypeople.showninfoaboutpeople()

#comment