from googletrans import Translator

translator = Translator()

language = {
    "bn": "Bangla",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "hi": "Hindi",
    "hu": "Hungarian",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "ml": "Malayalam",
    "nl": "Dutch",
    "pl": "Polish",
    "pt": "Portuguese",
    "ru": "Russian",
    "ta": "Konkani",
    "la": "Latin",
    "ar": "Arabic",
    "tr": "Turkish",
    "de": "German",
    "fi": "Finnish",
    "zh": "Chinese",
}

allow = True
while allow:
    usercode = input(f"Enter language code. To see language codes, enter 'options' \n")
    
    if usercode == "options":
        print("Code :  Language")
        for i in language.items():
            print(f"{i[0]}=> {i[1]}")
        print()
        
    else:
        for lancode in language.keys():
            if lancode == usercode:
                print(f"You have selected {language[lancode]}")
                allow = False
        
        if allow:
            print("Invalid code. Please try again")
            
while True :
    string = input("\nWrite the text you want to translate : \n To exit , enter 'exit'. \n")
    
    if string == "exit":
        print("Exited the program")
        
    translated = translator.translate(string, dest = usercode)
    
    print(f"\n{language[usercode]} translation: {translated.text}\n")
    print(f"Pronounciation : {translated.pronunciation}\n")
    
    for i in language.items():
        if translated.src == i[0]:
            print(f"Original language : {i[1]}\n")