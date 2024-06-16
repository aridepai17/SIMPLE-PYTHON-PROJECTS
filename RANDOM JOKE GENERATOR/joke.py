import requests 

def jokes():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    return response.json()

def main():
    while True:
        userinput = input("Press Enter to generate a joke or 'q' to quit: ")
        if userinput.lower() == "q":
            break
        jokedata = jokes()
        
        if jokedata["type"] == "single":
            print(f"{jokedata['joke']}")
        else:
            print(f"Setup: {jokedata['setup']}")
            print(f"Punchline: {jokedata['delivery']}")
    print("Random Joke Generator")
    jokedata = jokes()
    
    if jokedata["type"] == "single":
        print(f"{jokedata['joke']}")
    else:
        print(f"Setup: {jokedata['setup']}")
        print(f"Punchline: {jokedata['delivery']}")
        
if __name__ == "__main__":
    main()

