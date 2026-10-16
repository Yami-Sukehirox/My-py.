username = input("Enter your username: ")

if len(username) > 15:
    print("Character must not contain 15")
elif not username.find(" ") == -1:
    print("Your username must not contain a space")
elif not username.isalpha():
    print("Your username must not contain a number")        
else:
    print(f"Welcome to FaceBook {username}.")    