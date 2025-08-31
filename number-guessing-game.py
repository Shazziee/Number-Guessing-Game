import random
from colorama import Fore, Style, Back
    
def get_name(): 
    user_name = input("Hey, what is your name? ")
    return user_name.capitalize()  # this capitalises the first letter only

def generate_computer_name():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_name = ""
    for _ in range(0, 6):  # _ is used when we don't need to use that variable but we need the loop to run x times, it's python convention for "idc about this variable"
        computer_name = letters[random.randint(0, 25)]
        new_name = new_name + computer_name
    return new_name.capitalize()

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
    computer_name = generate_computer_name()
    greet_user(NAME, computer_name)
    while True:
        print(f"Match: {match_counter}")
        user_number_guess = guess_number()
        computer_number = choose_number()
        display_numbers(user_number_guess, computer_number)
        print_outcome(user_number_guess, computer_number)
        match_counter += 1
run_game()
