class Animal:
    zoo_name = "Hayaton" # תכונת מחלקה, ערך משותף לכל החיות

    def __init__(self, name, hunger=0):
        self.name = name
        self.hunger = hunger

    def getname(self):
        return self.name

    def is_hungry(self):
        return self.hunger > 0

    def feed(self):
        if self.is_hungry():
            self.hunger = self.hunger - 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    # הוספת חיות לרשימת החיות
    Brownie = Dog("Brownie", 10)
    Zelda = Cat("Zelda", 3)
    Stinky = Skunk("Stinky")
    Keith = Unicorn ("Keith", 7)
    Lizzy = Dragon ("Lizzy", 1450)

    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)
    zoo_lst = [Brownie, Zelda, Stinky, Keith, Lizzy , doggo, kitty, stinky_jr, clair, mcfly]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(f"{type(animal).__name__} {animal.getname()}")
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    # הדפסת שם גן החיות פעם אחת בסוף התוכנית
    print(f"The zoo's name is : {Animal.zoo_name}")


if __name__ == "__main__":
    main()

