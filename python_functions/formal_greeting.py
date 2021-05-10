def formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

#mustard = formal_greeting("Mustard", "Colonel")
#print(mustard)

def ask_for_info():
    user_name = input("What is your name? ")
    user_title = input("What is your title? ")

    print(formal_greeting(user_name, user_title))

ask_for_info()