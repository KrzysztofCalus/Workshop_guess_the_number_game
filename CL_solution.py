import random

def get_number():
    """
    Get number from user. Allow to give only number.
    :return: integer; user guess number
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            "It's not a number"
    return result

def guess_the_number():
    """
    Main function of application. Checking user guess to secret number
    """
    secret_number = random.randint(1, 100)
    user_number = get_number()
    while secret_number != user_number:
        if secret_number < user_number:
            print("To big")
        else:
            print("To small")
        user_number = get_number()
    print("You win!")

if __name__ == '__main__':
    guess_the_number()