from googletrans import Translator, LANGUAGES

translator = Translator()

languageoptions = LANGUAGES.items()
languagecodes = []
languagenames = []

def errors():
    print("Unknown Language. Wisely choose from the list.")
    print(f"Language Codes: {languagecodes}\n")
    print(f"Or from Language Names: {languagenames}")
    
for options in languageoptions:
    languagecodes.append(options[0])
    languagenames.append(options[1].lower())
    
translatingfrom = input("Enter the language you want to translate from: ").lower()
word = input("Enter the text you want to translate: ").lower()
translatingto = input("Enter the language you want to translate to: ").lower()

try:
    if translatingfrom and translatingto in languagecodes or languagenames:
        translation = translator.translate(word, src = translatingfrom, dest = translatingto).text
        print(translation.capitalize())
    else:
        errors()

except:
    print("An error occured. Please try again.")
    errors()
    