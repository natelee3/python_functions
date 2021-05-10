#1. Madlib function

def madlib(name, subject):
    print("%s's favorite subject is %s." % (name, subject))

# # madlib("Sarah", "geometry")



#2. Celsius to Farenheit conversion
# #Write a function that converts temp in C to F and returns the value

def c_to_f(celsius):
    print((celsius * 9/5) +32)

# # c_to_f(0)



#3. Farenheit to Celsius conversion
# #Write a function that converts temp in F to C

def f_to_c(faren):
    print((faren - 32) * 5/9)

# # f_to_c(32)



#4. Is Even
# #Accepts a number and returns a boolean

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# is_even(2)
# is_even(5)



#5. Is Odd
#Uses the is_even function

def is_odd(number):
    test = is_even(number)
    if test == True:
        return False
    else:
        return True  

# is_odd(5)
# is_odd(4)



#6. Only Evens
#Accepts a list of numbers and returns a list of only even ones

def only_evens(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num)
    print(new_list)

# only_evens([11, 20, 42, 97, 23, 10])



#7. Only Odds
#Accepts a list of numbers and returns a list of only the odd ones

def only_odds(list):
    new_list = []
    for num in list:
        test = is_odd(num)
        if test == True:
            new_list.append(num)
    print(new_list)

only_odds([11, 20, 42, 97, 23, 10])