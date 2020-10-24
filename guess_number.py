# MODULES ARE IMPORTED HERE
import random

# USER DEFINED FUNCTIONS ARE HERE

def hello() -> tuple:
    # INTRUDUCTION AND GETTING INPUT FROM USER
    print("Hello! Thank you for playing my guessing number game")
    print("Please enter the range for guessing. e.g. 1 - 20")

    # CHANGING INPUT() -> STR TO INT
    try:
        start_range = int(input("Please enter starting value: "))
        end_range = int(input("Please enter emd value here: "))
    
        print(f"I'm thinking of a number between {start_range} and {end_range}!")
        return (start_range, end_range)
    except ValueError as e:
        print("You didn't enter a number! Game terminated. Ty again...", e)


def generate_number(x: int, y: int) -> int:
    # I USE RANDOM.RANDINT() TO GENERATE A RANDOM NUMBER BUT THIS FUNCTION COULD BE SKIPPED
    # FOR SORTING OUT MY CODE I USED FUNCTION TO CONTROL FLOW OF MY PROGRAM.
    
    guess_int = random.randint(x, y)    
    return guess_int


def check_guess(guess: int, random_num: int) -> str:
    # WE WANT TO CHECK THE USER GUESS AGAINST OUR NUMBER GENERATED SO
    
    if guess == random_num:
        return "You've guessed correctly!"
    elif guess < random_num:
        return "Too low"
    elif guess > random_num:
        return "Too high"


# ENTRY POINT TO OUR SCRIPT
def main():
    # WE'RE UNPACKING TUPLE FROM OUR HELLO FUNCTION RETURN STATEMENT
    # TO USE IT IN GENERATE_NUMBER FUNCION.
    try:
        start, end = hello()
    
        # GETTING OUR RANDOM NUMBER, TYPE -> INT
        RANDOM_NUMBER = generate_number(start, end)
        # print(RANDOM_NUMBER) for testing only
    
        # NUM OF TRIES, TYPE -> INT
        numberGuesses = 5

        while True: # RUNNING THE GAME
            # GETTING INPUT FROM THE USER, TYPE CHANGE STR -> INT
            try: # IF THE USER DONT ENTER A NUMBER - DONT BREAK THE CODE! JUST CONTINUE
                guess = int(input("Enter your guess here or -1 to quit: "))

                # TESTING IF USES ISHES TO EXIT GAME
                if guess == -1:
                    print("You've left the game!")
                    break
    
                else:
                    # RESULT IS A TEST BETEEN GUESS AND RANDOM_NUMBER
                    result = check_guess(guess, RANDOM_NUMBER)

                    # TEST CASES 
                    if result == "Too low":
                        numberGuesses -= 1
                        print(f"Try higher, you guess was {result}. You have {numberGuesses} tries left!")              
                
                        if numberGuesses == 0:
                            print(f"The random number was: {RANDOM_NUMBER}, you've ran out of tries. Game ended!")
                            break

                    elif result == "Too high":
                        numberGuesses -= 1
                        print(f"Try lower, you guess was {result}. You have {numberGuesses} tries left!")              
                
                        if numberGuesses == 0:
                            print(f"The random number was: {RANDOM_NUMBER}, you've ran out of tries. Game ended!")
                            break
                    else:
                        numberGuesses -= 1
                        print(f"{result} you had {numberGuesses} tries left!")
                        break
            except ValueError as e:
                print("Enter a number...", e)
                
    # WE CAN'T UNPACK HELLO FUNCTION BECAUSE OF ERROR, RETURN STATEMENT RETURNS NONTYPE OBJECT - IT BREAKS OUR CODE
    # SO I CONTROL IT HERE.
    except TypeError: pass
        
   
# RUNNING THE PROGRAM
if __name__ == '__main__':
    main()
