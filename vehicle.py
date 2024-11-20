class vehicle:
    def __init__(self, given_name, given_speed, given_size):
        self.name = given_name
        self.size = given_size
        self.speed = given_speed

        def switch_on(self):
            print(f"You have switched on your {self.name}.")
        
        def drive(self):
            print(f"You are now driving your {self.name}!!!")

        def fix(self):
            print(f"You are fixing your {self.name} now")

class Car(vehicle):
    def switch_on(self):
        print(f"You have switched on your {self.name}.")
    def drive(self):
        print(f"You are now driving your {self.name}!!!")
    def fix(self):
        print(f"You are fixing your {self.name} now")
    def refuel(self):
        print(f"You are now refuelling your {self.name}")

class motorbike(vehicle):
    def switch_on(self):
        print(f"You have switched on your {self.name}.")
    def drive(self):
        print(f"You are now driving your {self.name}!!!")
    def fix(self):
        print(f"You are fixing your {self.name} now")
    def brake(self):
        print(f"You pressed down on the brakes of your {self.name}.")

Taxi = Car('toyota', '30 m/s', '2m')
Taxi.drive()
Taxi.refuel()

Motor = motorbike('loud bike', '40m/s', '0.8m')
Motor.drive()
Motor.brake()