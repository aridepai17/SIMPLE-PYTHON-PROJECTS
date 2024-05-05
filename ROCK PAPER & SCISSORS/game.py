import random
userwins = 0
computerwins = 0

options = ["rock" , "paper" , "scissors"]

while True:
    userinput = input("Type Rock/Paper/Scissors or Q to Quit : ").lower()
    if userinput == "q":
        break
        
    if userinput not in ["rock" , "paper" , "scissors"]:    
        continue
    
    randomnumber = random.randint(0,2)
    # rock : 0 , paper : 1 , scissors : 2
    computerguess = options[randomnumber]
    print("Computer guessed", computerguess + ".")
    
    if userinput == "rock" and computerguess == "scissors":
        print("You Won!")
        userwins += 1
    
    elif userinput == "paper" and computerguess == "rock":
        print("You Won!")
        userwins += 1
        
    elif userinput == "scissors" and computerguess == "paper":
        print("You Won!")
        userwins += 1
      
    if userinput == computerguess:
        print("It's a Draw!")
    
    else:
        print("You Lost!")
        computerwins += 1
        
print("You Won" , userwins , "times.")
print("The Computer Won", computerwins , "times.")
print("GoodBye!")
       