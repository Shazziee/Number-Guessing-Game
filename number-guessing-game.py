import random
from colorama import Fore, Style, Back
CONSONANTS = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
VOWELS = ["a", "e", "i", "o", "u"]  # good practice to put constants at the top
NUMBER_OF_CONSONANT_VOWEL_PAIRS = 3  
    
def get_name(): 
    user_name = input("Hey, what is your name? ")
    return user_name.capitalize()  # this capitalises the first letter only

def generate_computer_name():  # docstrings are more specified comments, and can only be written under functions. 
    '''

    The for loop iterates over our chosen number of digits, creating 3 pairs of each (vowels and consonants). 
    Lists are indexxed into a randomiser, generating random letters. Then, both characters are joined and the accumulator is updated with them. 
    This is so that the name appears more natural as it's composed of vowel-consonant pairs.

    '''
    new_name = ""
    for _ in range (0, NUMBER_OF_CONSONANT_VOWEL_PAIRS):   # it will iterate twice, 3 rounds each, so we get a 6 letter name
        random_consonant = CONSONANTS[random.randint(0, len(CONSONANTS) - 1)]   # to make name look more realistic 
        random_vowel = VOWELS[random.randint(0, len(VOWELS) - 1)]
        constant_vowel_pair = random_consonant + random_vowel
        new_name += constant_vowel_pair
    return new_name.capitalize()  # capitalises the first letter of a word

def greet_user(NAME, computer_name):
    formatted_username = f"{Fore.GREEN}{NAME}"
    formatted_computername = f"{Fore.BLUE}{computer_name}"  # makes code cleaner 
    reset_colour = Style.RESET_ALL
    print(f"Hello {formatted_username}{reset_colour}, I'm {formatted_computername}{reset_colour}, welcome to my guessing game!")
    
def guess_number():
    game_rules = "Please enter a number between 1 and 15: " # this variable will create less repition. if we wanna modify the rules, now we only have to change 1 string not 2
    try:
        number = int(input(game_rules))
        while number > 15 or number < 1:
            number = int(input(game_rules))
    except ValueError:
        number = int(input("Please enter a number only: "))
    return number 

def choose_number(): 
    random_number = random.randint(1, 15) # generates random integers
    return random_number

def display_numbers(user_number_guess, computer_number):
    print(f"You have chosen: {user_number_guess}")    
    print(f"Computer has chosen: {computer_number}")  

def print_outcome(user_number_guess, computer_number):
    if user_number_guess == computer_number:
        print(f"{Back.GREEN}{Fore.GREEN}Congratulations, you have won this game!{Style.RESET_ALL}")
    else:
        print(f"{Back.RED}{Fore.RED}You have failed, better luck next time!{Style.RESET_ALL}")

def run_game():
    match_counter = 1
    NAME = get_name()
    COMPUTER_NAME = generate_computer_name()
    greet_user(NAME, COMPUTER_NAME)
    infinite_rounds = input("Would you like to play infinitely? ") 
    if infinite_rounds == "Yes" or infinite_rounds == "yes":
        while True:
            print(f"Match: {match_counter}")
            user_number_guess = guess_number()
            computer_number = choose_number()
            display_numbers(user_number_guess, computer_number)
            print_outcome(user_number_guess, computer_number)
            match_counter += 1
    else:
        ask_how_many_matches = int(input("How many matches would you like to play? "))
        for _ in range(ask_how_many_matches):
            print(f"Match: {match_counter}")
            user_number_guess = guess_number()
            computer_number = choose_number()
            display_numbers(user_number_guess, computer_number)
            print_outcome(user_number_guess, computer_number)
            match_counter += 1
    print("Thank you for playing!😊")

run_game()
