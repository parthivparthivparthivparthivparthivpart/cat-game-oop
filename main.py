from cat import Cat

print("Welcome to Parthiv Dev Chowdhury's game of cats")

name = input("Enter the cat's name: ")
colour = input("enter thy cats colour: ")
my_cat = Cat(name, colour)
while True:
    action = input("""
What would you like to do:
1. Train intelligence
2. Feed
3. Play
4. Sleep and defend
5. Slay enemies
""")
    
    if action == "1":
        my_cat.train()
    if action == "2":
        my_cat.feed()
    if action == "3":
        my_cat.play()
    
