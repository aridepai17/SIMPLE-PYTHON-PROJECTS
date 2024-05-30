import random 
import time 

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "A watched pot never boils.",
    "Actions speak louder than words.",
    "Beauty is in the eye of the beholder.",
    "Better late than never.",
    "The best preparation for tomorrow is doing your best today.",
    "Cleanliness is next to godliness.",
    "Birds of a feather flock together.",
    "The early bird catches the worm.",
    "The fool doth think he is wise, but the wise man knows himself to be a fool.",
    "The greatest glory in living lies not in never falling, but in risin every time we fall."    
]

def typingtest():
    sentence= random.choice(sentences)
    print("\n Typing Test.")
    print("Type the following sentence as quickly and accurately as possible.\n")
    print(sentence)
    input("\nPress Enter when you are ready.")
    
    starttime = time.time()
    userinput = input("\nType the sentence here: ")
    endtime = time.time()
    timetaken = endtime - starttime
    
    accuracy = sum(1 for a, b in zip(sentence, userinput)if a == b) / len(sentence) * 100
    
    print(f"\nResults: ")
    print(f"Time taken: {timetaken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    
    if userinput == sentence:
        print("Perfect! You are a typist.")
    else:
        print("There are some errors in your typing. Please try again.")
        
if __name__=="__main__":
    typingtest()
    
    
    