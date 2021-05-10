def formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

#mustard = formal_greeting("Mustard", "Colonel")
#print(mustard)

def ask_for_info_dictionary():
    user_name = input("What is your name? ")
    user_title = input("What is your title? ")
    return {
        "name": user_name,
        "title": user_title
    }

user_info = ask_for_info_dictionary()
greeting = formal_greeting(user_info["name"], user_info["title"])
print(greeting)