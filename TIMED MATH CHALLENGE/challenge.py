import random
import time

OPERATORS = ["+" , "-" , "*"]
MINOPERAND = 3
MAXOPERAND = 12
TOTALPROBLEMS = 15

def generateproblem():
    left = random.randint(MINOPERAND , MAXOPERAND)
    right = random.randint(MINOPERAND , MAXOPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr , answer

wrong = 0
input("Press Enter to start!")
print("------------------------------------")

starttime = time.time()

for i in range(TOTALPROBLEMS):
    expr , answer = generateproblem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
        
endtime = time.time()
totaltime = round(endtime -  starttime, 2)

print("----------------------------------------")
print("Well Done! You completed in ", totaltime, "seconds!")
