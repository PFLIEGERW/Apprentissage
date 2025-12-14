import random
randomNumber = random.randint(1,10)
guess = 99
while guess != randomNumber:
    guess = int(input("Guess the number between 1 and 10 : "))
    if guess == randomNumber:
        print("Correct")
    else:
        print("Try again")