class Device:
    def __init__(self, given_height, given_width, given_name):
        self.height = given_height
        self.width = given_width
        self.name = given_name
    
    def power_on(self):
        print("Device has turned on!!!")

class computer(Device):

    def power_on(self):
        print("Computer has turned on!!!")
    
    def shut_down(self):
        print("Computer has been shut down.")
    
    def open_app(self):
        print("YOu have opened an app.")

Pc = computer('0.5m', '0.5m', 'HP')
Pc.power_on()
Pc.open_app()
Pc.shut_down()