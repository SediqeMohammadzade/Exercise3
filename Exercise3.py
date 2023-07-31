print("Hello to this game")
print("we'll give you a number between 1_6, if that number is 6 you'll have another chance")

choice = int(input("select 1 if you want to play otherwise press 2:"))

import random
while True:
 
    if choice == 1:
        a = random.randint(1,6)
        print(a)

    if a == 6:
        print("another chance:")
        a = random.randint(1,6)
        print(a)
    else:
        break
    if choice == 2:
        break 
    else:

        print("Exit")