#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random
number=random.randrange(1,10)
guess=0
count=0
while guess != number and guess != "exit":
    guess = input("please guess a number between 1 and 9.when you want to end the game print'exit':")
    if guess=="exit":
        print("Game Over")
        break
    guess=int(guess)
    count += 1
    if guess not in range(1,10):
        print("you have to guess a number between 1 and 9")
    elif guess>number:
        print("you hane guessed too high")
    elif guess<number:
        print("you have guessed too low")
    else:
        if count == 1:
            print("you rock! you have got it at the first try! ")
        elif count<=3:
            print("Well done! you have got it in just {} tries".format(count))
        elif count>3:
            print("you have got it! it took you {} tries!.".format(count))
