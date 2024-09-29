from textblob import TextBlob
import random

# Song dataset categorized by mood
songs = {
    "happy": [
        "Can't Stop the Feeling - Justin Timberlake",
        "Good as Hell - Lizzo",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "I Gotta Feeling - The Black Eyed Peas",
        "On Top of the World - Imagine Dragons",
        "Shut Up and Dance - WALK THE MOON",
        "Levitating - Dua Lipa",
        "Dynamite - BTS",
        "Feel It Still - Portugal. The Man",
        "Sugar - Maroon 5"
    ],
    "sad": [
        "When the Party's Over - Billie Eilish",
        "Someone Like You - Adele",
        "The Night We Met - Lord Huron",
        "All I Want - Kodaline",
        "Let Her Go - Passenger",
        "Young and Beautiful - Lana Del Rey",
        "Tears Dry on Their Own - Amy Winehouse",
        "Liability - Lorde",
        "I Found - Amber Run",
        "Supermarket Flowers - Ed Sheeran"
    ],
    "angry": [
        "Kill This Love - BLACKPINK",
        "Blow Me (One Last Kiss) - P!nk",
        "The Kill - Thirty Seconds to Mars",
        "Break Stuff - Limp Bizkit",
        "Run the World (Girls) - Beyoncé",
        "Smells Like Teen Spirit - Miley Cyrus (Live Cover)",
        "I Hate Everything About You - Three Days Grace",
        "Duality - Slipknot",
        "Sabotage - Beastie Boys (2009 Remaster)",
        "DNA - Kendrick Lamar"
    ],
    "calm": [
        "Weightless - Marconi Union",
        "Night Owl - Galimatias",
        "Sunset Lover - Petit Biscuit",
        "Holocene - Bon Iver",
        "Cold Little Heart - Michael Kiwanuka",
        "Everything I Wanted - Billie Eilish",
        "The Less I Know the Better - Tame Impala",
        "Bloom - The Paper Kites",
        "Telegraph Ave - Childish Gambino",
        "Slow Dancing in the Dark - Joji"
    ],
    "motivated": [
        "Stronger - Kanye West",
        "Eye of the Tiger - Survivor",
        "Lose Yourself - Eminem",
        "Unstoppable - Sia",
        "Hall of Fame - The Script ft. will.i.am",
        "Remember the Name - Fort Minor",
        "Can't Hold Us - Macklemore & Ryan Lewis",
        "Survivor - Destiny's Child",
        "Born This Way - Lady Gaga",
        "Roar - Katy Perry"
    ],
    "romantic": [
        "Perfect - Ed Sheeran",
        "All of Me - John Legend",
        "Just the Way You Are - Bruno Mars",
        "Lover - Taylor Swift",
        "Adore You - Harry Styles",
        "Kiss Me - Ed Sheeran",
        "La Vie En Rose - Daniela Andrade",
        "10,000 Hours - Dan + Shay, Justin Bieber",
        "Stay With Me - Sam Smith",
        "Love on Top - Beyoncé"
    ],
    "nostalgic": [
        "Somewhere Only We Know - Keane",
        "Wake Me Up When September Ends - Green Day",
        "Photograph - Ed Sheeran",
        "Youngblood - 5 Seconds of Summer",
        "We Are Young - fun. ft. Janelle Monáe",
        "The Nights - Avicii",
        "Memories - Maroon 5",
        "Stressed Out - Twenty One Pilots",
        "Home - Edward Sharpe & The Magnetic Zeros",
        "7 Years - Lukas Graham"
    ],
    "relaxed": [
        "Location - Khalid",
        "Electric Feel - MGMT",
        "Coffee - Miguel",
        "Malibu - Miley Cyrus",
        "Ocean Eyes - Billie Eilish",
        "Sunflower - Rex Orange County",
        "Put Your Records On - Corinne Bailey Rae",
        "Breathe - Jax Jones ft. Ina Wroldsen",
        "Riptide - Vance Joy",
        "Island in the Sun - Weezer"
    ]
}

# Function to analyze the sentiment and determine mood
def analyze_mood(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0.5:
        return "happy"
    elif sentiment > 0:
        return "calm"
    elif sentiment < -0.5:
        return "sad"
    elif sentiment == 0:
        return "angry"
    elif sentiment > -0.5:
        return "nostalgic"
    else:
        return "motivated"

# Function to generate a playlist based on the mood
def generate_playlist(mood):
    if mood in songs:
        print(f"\nDetected mood: {mood.capitalize()}")
        print("Here's a playlist for you:")
        playlist = random.sample(songs[mood], 3)  # Select 3 random songs from the mood category
        for song in playlist:
            print(f" - {song}")
    else:
        print("Mood not recognized.")

# Main program to run the mood-based playlist generator
if __name__ == "__main__":
    print("Welcome to the Mood-Based Playlist Generator!")
    user_input = input("Describe your mood or type something: ")

    # Analyze the user's input to determine the mood
    mood = analyze_mood(user_input)
    
    # Generate and display a playlist based on the detected mood
    generate_playlist(mood)