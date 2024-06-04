"""Whenever you create an account on a site by entering your username and
password , the site ensures that the password you are trying to save is
strong. The strength of a password is determined by several factors"""

"""In this project, we are going to mimic the site, functionality into a console-based
Python program.The script will check the strength of the password that the user will enter.
The script will show the number of alphabets, numbers, special characters, and whitespace characters
present within the password and will accordingly mark the password's strength."""

"""The best password will be the one containing atleast one UPPERCASE letter, one LOWERCASE letter, 
one DIGIT, one SPECIAL CHARACTER and atleast one WHITESPACE character."""

specialcharacters="!@#$%^&*()_+{}|:<>?"

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    password = input("Enter your password: ")
    checker(password)
    
def checker(password):
    checking = {
        "digit" : False,
        "lowercase" : False,
        "uppercase" : False,
        "special" : False,
        "whitespace" : False
    }
    
    for c in password:
        if not(checking["digit"]):
            if c.isdigit():
                checking["digit"] = True
        if not(checking["lowercase"]):
            if c.islower():
                checking["lowercase"] = True
        if not(checking["uppercase"]):
            if c.isupper():
                checking["uppercase"] = True
        if not(checking["special"]):
            if c in specialcharacters:
                checking["special"] = True
        if not(checking["whitespace"]):
            if c.isspace():
                checking["whitespace"] = True
                
    for check in checking.keys():
        if checking[check]:
            print(color.BOLD + "{}: ".format(check) + color.GREEN + "OK" + color.END)
        else:
            print(color.BOLD + "{}: ".format(check) + color.RED + "NOT OK" + color.END)
        
if __name__ == "__main__":
    main()