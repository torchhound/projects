import random

random.seed()

def cows(lst):
    cows = 0
    for x in rint:
        for y in lst:
            if x == y:
                cows += 1
    return cows

def bulls(lst):
    bulls = 0
    for x in lst:
        if x in rint:
            bulls += 1
    return bulls

def game():
    print("Cows and Bulls Game")
    rint = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]
    guesses = 0
    win = False
    while win == False:
        print("Guess a number or type help:\n")
        user = input(">>> ")
        if user == "help" or "Help":
            print("Type a 4 digit number, if a number is in the correct place in your guess you get a cow, if a number matches any of the numbers but is in the wrong place you get a bull")
        else:
            if cows(user) == 4:
                print("A winner is you!")
                win = True
            else:
                print("{} cows, {} bulls".format(cows(user), bulls(user)))
        guesses += 1
    print(guesses)

game()

