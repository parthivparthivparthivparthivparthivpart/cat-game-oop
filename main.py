from cat import Cat
from cat import Eldritch_God
import re
import random
print("Welcome to Parthiv Dev Chowdhury's game of cats")
def stats():
    print(f"""Age: {my_cat.age}
Intelligence: {my_cat.intelligence}
Weight: {my_cat.weight}
Energy: {my_cat.energy}
combat: {my_cat.combat}
sanity: {my_cat.sanity}
Money: {my_cat.money}
""") 
def miracle():
     a = random.randint(1, 10)
     if a == 7:
          print("Your eldritch God peformed a miracle!!!!!")
          my_cat.weight += 1
          my_cat.intelligence += 1
          my_cat.energy += 15
          my_cat.combat += 2
          my_cat.sanity += 10
          my_cat.money += 100
name = input("Enter the cat's name: ")
colour = input("enter thy cats colour: ")
if re.search(r'[^a-zA-Z0-9]', name):
    print("We have deduced that your cat is actually an eldritch God")
    while True:
        
        my_cat = Eldritch_God(name, colour)
        action = input("""
What would you like to do:
1. Train intelligence
2. Feed
3. Play
4. Sleep and defend
5. Slay enemies
6. shop
""")
        if action == "1":
            my_cat.train()
            stats()
            miracle()
        if action == "2":
            my_cat.feed()
            stats()
            miracle()
        if action == "3":
            my_cat.play()
            stats()
            miracle()
        if action == "4":
            my_cat.sleep()
            stats()
            miracle()
        if action == "5":
            my_cat.fight()
            stats()
            miracle()
        if my_cat.sanity > 0:
            print("Your cat, also known as Azathoth, has now fully awoken and had destroyed the known universe")
        if action == '6':
            buy = input("""
What do you want to buy?:
1. The Catkiller killer (250)
2. Eldritchify (250)
3. End the universe (500))
""")
            if buy == '1':
                if my_cat.money >= 250:
                    print("You killed the catkillers!!!!")
                    break
                else: print("Not enough money")
            if buy == '3':
                if my_cat.money >= 500:
                    print("You destroyed the entire universe for what? your cat also died")
                    break
                else: print("Not enough money")
if name.isalpha():
    my_cat = Cat(name, colour)
    while True:
        action = input("""
What would you like to do:
1. Train intelligence
2. Feed
3. Play
4. Sleep and defend
5. Slay enemies
6. shop
""")

        if action == "1":
            my_cat.train()
            stats()
        if action == "2":
            my_cat.feed()
            stats()
        if action == "3":
            my_cat.play()
            stats()
        if action == "4":
            my_cat.sleep()
            stats()
        if action == "5":
            my_cat.fight()
            stats()
        if my_cat.sanity < 0:
             print("Your cat becomes insane and suddenly enlarges, and eats you")
             break
        if action == '6':
            buy = input("""
What do you want to buy?:
1. The Catkiller killer (250)
2. Eldritchify (250)
3. End the universe (500))
""")
            if buy == '1':
                if my_cat.money >= 250:
                    print("You killed the catkillers!!!!")
                    break
                else: print("Not enough money")
            if buy == '2':
                if my_cat.money >= 250:
                    print("You transformed your cat into a GOD")
                    my_cat = Eldritch_God
                else: print("Not enough money")
            if buy == '3':
                if my_cat.money >= 500:
                    print("You destroyed the entire universe for what? your cat also died")
                    break
                else: print("Not enough money")
        if my_cat.age > 100:
            print("Your cat grew old and you both died happily")
            break


