class Cat:
    # the constructor will create a cat for us in code
    # to create a cat we need given_name and given_colour
    #self is the cat that we are creating
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour 
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    
    def train(self):
        print(f"{self.name} is doing push-ups...")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1
    def feed(self):
        print(f"{self.name} ate some freshly cooked ravioli...")
        self.energy += 10
        self.weight += 1
        self.age += 0.1
    
    

# we will now make two cats
# These are called instances
# each one is an instance of cats

