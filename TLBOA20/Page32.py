username = "James"
password = "myPasswordIsDog!"
pass_in = ""
tries = 0

while tries < 3 and pass_in != password:
    user_in = input("Enter the username: ")
    pass_in = input("Enter the password: ")
    if user_in == username:
        if pass_in == password:
            print("Logged in")
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")
        
    tries = tries+1