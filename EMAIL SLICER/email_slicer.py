def emailslicer(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return "Invalid email format"
    
email = input("Enter your email: ")
username, domain = emailslicer(email)

if username != "Invalid email format":
    print(f"Username : {username}")
    print(f"Domain : {domain}")
else:
    print(username)