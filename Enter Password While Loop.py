

# set password
password = "password123"

# set number of tries
tries = 5

# loop until user enters correct password or runs out of tries
while tries > 0:
    # get user input
    user_input = input("Enter password: ")

    # check if password is correct
    if user_input == password:
        print("You are in the system.")
        break
    else:
        tries -= 1
        if tries == 0:
            print("You have been kicked out of the system.")
        else:
            print("Incorrect password. You have", tries, "tries left.")
            choice = input("Do you want to re-enter the password? (Y or N) ")
            if choice.upper() != "Y":
                break