import random

pc_number = random.randint(1, 101)

while True:
    user_number = input("Guess the number:")
    try:
        user_number = int(user_number)
    #    print(pc_number)
        if user_number == pc_number:
            print("You win!")
            break
        elif user_number > pc_number:
            print("To big")
        else:
            print("To small")
    except ValueError:
        print("It's not a number!")


