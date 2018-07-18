#this code is called as gues the number,
#you have 6 tries to win


import random

guessTaken = 0

print(" hello what is your name")
myname = input()

number = random.randint(1,20)
print("well ," + myname + ", I am thinking of a number between 1 and 20.")

while guessTaken < 6:
    print("take a guess") #there must be 4 spaces in front of print
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print("your guess is too low.")

    if guess >number:
        print("your guess is too high.")

    if guess == number:
        break
if guess == number:
    guessTaken = str(guessTaken)
    print("good job," + myname + " you guess my number in " + guessTaken + " guesses!")
if guess != number:
    number = str(number)
    print(" nope , the number that i was thinking of  was" + number)
