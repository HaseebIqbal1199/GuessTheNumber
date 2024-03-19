from random import *

def sys_ai():
    random_number = randrange(1,100)
    return random_number

sys_number = sys_ai()
counter = 0

def User_input():
    
    user_input = input("Enter your Guess : ")
    return user_input

def validator(x,y):
    if (int(x) != y):
        if(int(x) < y):
            print("Guessing Small.....")
            tries_count()
        else:
            print("Guessing Big.......")
            tries_count()
    else:
        print("You are a Winner !")

def logic(z):
        player_number = User_input()
        validator(player_number,z)

def tries_count():
    tries = counter
    if(tries <= 5):
        tries = counter + 1
        print(tries)
        logic(sys_number)
    else:
        exit()


def main():
    print("Number Guessing Game !")
    print("* I thought a number you Guess it ")
    print("* Thinking..... ")
    print("* OK ! Now Guess? ")
    tries_count()

main()