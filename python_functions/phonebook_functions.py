phone_book = {}

def transition():
    pause = input("Press any key to continue.")
    print("\033c")

def option_one():
    lookup_name = input("Name to look up: ")
    fixed_name = lookup_name.lower()
    if fixed_name in phone_book:
        print("Number for " + lookup_name + ": " + phone_book[fixed_name])
    else:
        print("That name does not appear. Please choose option 2 to add a new entry.\n") 
    transition()

def option_two():
    new_name = input("Name to add: ")
    fixed_name = new_name.lower()
    if fixed_name in phone_book:
        print("That name is already in the phonebook. Try again. ")
    else: 
        phone_book[fixed_name] = input("Phone number to add for " + str(new_name) + ": ")
        print("New entry added to phonebook for " + new_name + ".")
    transition()

def option_three():
    delete_name = input("Name to delete: ")
    if delete_name in phone_book:
        del phone_book[delete_name]
        print(delete_name + " has been deleted.")
    else:
        print("That name doesn't appear in the phonebook. Try again.")
    transition()

def option_four():
    if phone_book != {}:
        print(phone_book)
    else:
        print("The phonebook is currently empty. ")
    transition()

def option_five():
    print("\033c")
    print("Thanks for using the phonebook app. Bye.")
    running = False

main_menu = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
"""


running = True

while running == True:

    print(main_menu)

    user_selection = int(input("What do you want to do? (1-5) "))

    if user_selection == 1:
        option_one()
    elif user_selection == 2:
        option_two()
    elif user_selection == 3:
        option_three()
    elif user_selection == 4:
        option_four()
    elif user_selection == 5:
        print("Thanks for using the phonebook app. Bye. \n")
        running = False    
    else:
        print("Please choose an option 1-5.")
        user_selection = input("What do you want to do? ")

