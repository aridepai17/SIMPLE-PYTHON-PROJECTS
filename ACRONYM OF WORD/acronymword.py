def getacronym(phrase):
    phrase = phrase.replace('of', ' ')
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

userinput = input("Enter a phrase: ")
acronym = getacronym(userinput)
print(f"Acronym of '{userinput}' is {acronym}") 
