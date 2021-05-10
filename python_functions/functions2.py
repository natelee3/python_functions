def upper_case(some_text):
    return some_text.upper()

user_input = input("Type a word of your choice: ")
print("User input is: " + user_input)

new_text = upper_case(user_input)
print("Upper-case version: " + new_text)