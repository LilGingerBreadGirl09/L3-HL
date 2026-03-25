def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter and integer! Geez people! o(≧口≦)o"

    # If the number need to be more than an
    # inter (ie: rounds / 'high number' )
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    # If the number need to be between low and High
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")


    # Set up error messages
    error = "Please enter an Integer! Geez people!o(≧口≦)o"

    while True:
        response = input(question).lower()

        # Check for infinite mode / exit mode
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            #Check response is more than the low number
            elif high is not None and response > high:
                print(error)

             #if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

#Main Routine goes here

#rounds = "test"
#while rounds != "":
   # rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")
    #print(f"You asked for {rounds}")

#low_num = int_check("Low number? ")
#print(f"You chose a low number of {low_num}")

#high_num = int_check("High number? ", low=1)
#print(f"You chose a high number of {high_num}")

#Check User guesses
guess = ""
while guess != "xxx":
    guess = int_check("Guess: ", low=0, high=10, exit_code="xxx")
    print(f"You guessed {guess}")
    print()

