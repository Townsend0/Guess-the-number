import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  \n
"""
d=random.randint(1,100)
def game(a):
    print(f'\nYou have {a} attempts to guess the number.')
    for e in range(1,a+1):
        b=True
        while b:
            c=int(input('\nmake a guess: '))
            if  c>=1 and c<=100:
                b=False
            else:
                print("\n( Invalid input )")
        if c>d and a-e:
            print(f"\nToo high!\n\nGuess again\n\nYou have {a-e} attempts remaining to guess the number.")
        elif c<d and a-e:
            print(f"\nToo low!\n\nGuess again.\n\nYou have {a-e} attempts remaining to guess the number.")
        elif c==d :
            return "\nYou win"
    return f"\nYou've run out of guesses, you lose.\n\nThe number was: {d}"

print(f"{logo}\nwelcome to the number guessing game!".title())
print('\nI\'m thinking of a number between 1 and 100.')
b=True
while b:
    b=False
    a=input('\nChoose a difficulty. type "easy" or "hard": ').lower()
    if a=='easy':
        print(game(10))
    elif a=='hard':
        print(game(5))
    else:
        print("\n( Invalid input )")
        b=True