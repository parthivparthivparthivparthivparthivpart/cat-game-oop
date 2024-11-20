class Person:
    def __init__(self, given_name):
        self.name = given_name
        self.water = 5
        self.thirst = 1
    
    def drink(self):
        self.water -= 1
        

