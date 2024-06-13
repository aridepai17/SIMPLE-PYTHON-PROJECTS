import pyfiglet

user_input = input("Enter the text to convert to font art: ")
font_art = pyfiglet.figlet_format(user_input)
print(font_art)