
def yes_no(question):
    """Checks if user enters yes / no"""
    while True:

        response  = input(question).lower()

        # Check if the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer the question, yes or no! Geez people! o(≧口≦)o")


def instructions():
    """prints instructions"""

    print("""
    *** Instructions ***

    To begin, choose the number of rounds
    and either customise the game parameters
    or go with the default game (where the
    secret number will be between 1 and 100).

    Then choose now many rounds you'd like to play!
     <enter> for infinite mode!

     Good luck Superstar!

    """)


# Check that users have entered a valid
# option based on a list
def int_check(question):
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 1. >:["

    while True:

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
               return response

        except ValueError:
            print(error)




# Main routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0

print("⬆️⬆️ WELCOME to the HIGHER Or lower GAME!!️⬇️⬇️")
print()

# Instructions
want_instructions = yes_no ("Do you want to see instructions? ")
print()

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

#Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#Game loop starts here
while rounds_played < num_rounds:

    rounds_played += 1

    # Round Headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played} (Infinite Mode)♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    user_choice = input("Choose: ")
    print(f"you chose {user_choice}")

    if user_choice == "xxx":
        break

    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


#Game loop ends here

#Game history / Statistics here