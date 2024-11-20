
class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def makeNoise(self):
        print("Meow")
    def play(self, cat):
        print(self.name + " Is playing with " + cat.name )
    def fight(self, dog):
        print(self.name + ' is fighting ' + dog.name)
class Dog(Cat):
    def __init__(self, name, colour, breed):
        super().__init__(name, colour)
        self.breed = breed
    def makeNoise(self):
        print("woof")
    def play(self, dog):
        super().play(dog)
    def fight(self, cat):
        super().play(cat)
    def statebreed(self):
        print(self.name + ' is a ' + self.breed)

myCat = Cat("Flakey", "Black")
myDog = Dog("Eddie", "Grey", "Pug")
neighbourCat = Cat("Garfield", "Ginger")
neighbourDog = Dog("Odie", "Brown", "Poddle")
myCat.makeNoise()
myDog.makeNoise()
myCat.play(neighbourCat)
myDog.play(neighbourDog)
myCat.fight(neighbourDog)
myDog.fight(neighbourCat)
myDog.statebreed()


    