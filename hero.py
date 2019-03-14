class Hero():
    """class to create hero for our game"""
    def __init__(self, name, level, rase):
        """initiate of hero"""
        self.name = name
        self.level = level
        self.rase = rase
        self.health = 100

    def show_hero(self):
        """print all parameter of this hero"""
        description = (self.name + "level is " + str(self.level) + "rase is " + self.rase + "health is" + str(self.health).title())
        print(description)

    def level_up(self):
        """"upgrade lvl for hero"""
        self.level = self.level+1

    def move(self):
        """start moving"""
        print("hero" + self.name + " start moving")

    def set_health(self, new_health):
        self.health = new_health

class superhero(Hero):
    """class to create superhero"""
    def __init__(self, name, level, rase, magiclevel):
        #Initiate superHero
        super().__init__(name,level, rase)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """use magic"""
        self.magic -=10

    def show_hero(self):
        """print all parameter of this hero"""
        description = (self.name + "level is " + str(self.level) + "rase is " + self.rase + "health is" + str(
            self.health) + "magic is " + str(self.magic).title())
        print(description)