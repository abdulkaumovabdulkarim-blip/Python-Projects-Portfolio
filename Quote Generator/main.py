# main.py
# PYTHON PROJECTS - "QUOTE GENERATOR"

# Abdulqayumov Abdukarim

import random
from quotes import QUOTES


# Main Menu Function and Get Category of Quote
def main_menu():
    print("Choose the one of these options or press Enter to get Random Quote")
    print("\t1. Inspirational/Motivational Quotes")
    print("\t2. Wisdom/Philosophy Quotes")
    print("\t3. Humor/Wit Quotes")
    print("\t4. Love/Relationships Quotes")
    print("\t5. Literature/Famous Quotes")
    category = input("[Enter number (1 - 5) or press Enter to get Random Quote]\n>  ")

    # Certain category (1-5) to check
    check_category = ["1", "2", "3", "4", "5"]

    # Set the category if user didn't give number (1-5)
    if category in check_category:
        category = int(category)
    else:
        category = random.randint(1, 5)
    
    return category


# Make sure to not to show the quote over again
showed_quotes_list = []
def get_quote(category):
    # Make global to access it even in the outside of function
    global showed_quotes_list

    # Get Random Quotes
    r_quoteNumber = random.randint(1, 10)
 
    quote = QUOTES[category]["quote"][r_quoteNumber]
    author = QUOTES[category]["name"][r_quoteNumber]

    # Check whether showed_quotes_list is full or not
    if len(showed_quotes_list) == 10:
        showed_quotes_list = []
    # Check whether quote has already shown in last 10 times or not
    if quote in showed_quotes_list:
        return get_quote(category)
 
    # Add new quote to the showed_quotes_list
    showed_quotes_list.append(quote)  

    return f'"{quote}"\n- {author}'


# --- PROGRAMM START ---
# Greeting the user
print("--- Welcome to the Daily Motivator ---")
print("[Press Enter to get inspired!]")
start = input("> ")

# Creating the loop
exit = True
while exit == True:
    
    # Get the category of quote from user
    category = main_menu()

    # Print the quote with its author 
    print(get_quote(category))

    # Ask for next quote or quit
    print("\n[Press Enter for another, or type 'quit' to exit]")
    exit_next = input("> ")
    exit_next.lower()
    if exit_next == "quit":
        exit = False
# --- EXIT ---
# Thanks
print("\nHave a productive day!😎")