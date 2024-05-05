import random

def roll():
    minvalue = 1
    maxvalue = 6
    return random.randint(minvalue, maxvalue)

# Get the number of players
while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid. Try again.")

# Initialize player scores
maxscore = 50
playerscores = [0 for _ in range(players)]

# Main game loop
while max(playerscores) < maxscore:
    # Loop through each player for their turn
    for playeridx in range(players):
        print(f"Player number {playeridx + 1}'s turn has just started!\n")
        currentscore = 0
        
        # Player's turn loop
        while True:
            shouldroll = input("Would you like to roll? (y) ")
            if shouldroll.lower() != 'y':
                # If the player doesn't want to roll, update their total score and exit the turn
                playerscores[playeridx] += currentscore
                print(f"Player {playeridx + 1}'s total score is: {playerscores[playeridx]}")
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                currentscore = 0  # Reset the current turn's score
                # Update the player's total score with the new current score (0 in this case)
                playerscores[playeridx] += currentscore
                print(f"Player {playeridx + 1}'s total score is: {playerscores[playeridx]}")
                break
            else:
                currentscore += value
                print(f"You rolled a {value}. Current turn score is: {currentscore}")
        
        # Check if this player has reached or exceeded the winning score
        if playerscores[playeridx] >= maxscore:
            break  # End the game loop if a player wins

# Determine the winner
winneridx = playerscores.index(max(playerscores))
print(f"Player {winneridx + 1} wins with a score of {playerscores[winneridx]}!")