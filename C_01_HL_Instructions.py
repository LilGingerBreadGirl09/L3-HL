#Instructions


def yes_no(question):
    """Checks if user enters yes / no"""
    while True:

        response  = input(question).lower()

        #Check if the user says yes / no / y / n
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


#Main routine
print()
print("⬆️⬆️ WELCOME to the HIGHER Or lower GAME!!️⬇️⬇️")
print()

# ask the user if they want instructions (check is they say yes / no)
want_instructions = yes_no ("Do you want to see instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program Continues")