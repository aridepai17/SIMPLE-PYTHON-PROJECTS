import random

number = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))
while number != guess:
    if guess < number:
        print("Too low")
        guess = int(input("Guess again: "))
    elif guess > number:
        print("Too high")
        guess = int(input("Guess again: "))
    else:
        break
print("You got it!")