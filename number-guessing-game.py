import random
from colorama import Fore, Style, Back
    
def get_name(): 
    user_name = input("Hey, what is your name? ")
    return user_name

def greet_user(NAME):
    print(f"Hello {Fore.GREEN}{NAME}{Style.RESET_ALL}, welcome to my guessing game!")
    
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
    greet_user(NAME)
    while True:
        print(f"Match: {match_counter}")
        user_number_guess = guess_number()
        computer_number = choose_number()
        display_numbers(user_number_guess, computer_number)
        print_outcome(user_number_guess, computer_number)
        match_counter += 1
run_game()
