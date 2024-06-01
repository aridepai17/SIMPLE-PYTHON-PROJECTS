from textblob import TextBlob

t = 1
while t:
    a = input("Enter the word to be checked for spelling: ")
    print("The word is: " + str(a))
    
    b = TextBlob(a)
    
    print("Corrected Text is: " + str(b.correct()))
    t = int(input("Enter 1 to continue and 0 to exit: "))
