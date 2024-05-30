import speech_recognition as sr

def recordvoice():
    microphone = sr.Recognizer()
    
    with sr.Microphone() as livephone:
        print("Adjusting for ambient noise, please wait...")
        microphone.adjust_for_ambient_noise(livephone, duration=1)
        
        print("Please say something: ")
        audio = microphone.listen(livephone)
        try:
            phrase = microphone.recognize_google(audio, language="en")
            return phrase
        except sr.UnknownValueError:
            return "I could not understand the audio"
        

if __name__ == "__main__":
    phrases = []
    while True:
        phrase = recordvoice()
        print(phrase)
        phrases.append(phrase)
        
        cont = input("Do you want to say something else? (yes/no): ").strip().lower()
        if cont != 'yes':
            break
