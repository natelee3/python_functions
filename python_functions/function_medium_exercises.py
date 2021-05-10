#1. Find the smallest number
# Accepts list and returns the smallest number

def smallest_number(list):
    smallest = list[0]
    for num in list:
        if num < smallest:
            smallest = num
    return smallest

# print(smallest_number([2, 3, 55, 4589, .5]))



#2. Find the largest number
#Accepts list and return the largest number

def largest_number(list):
    largest = list[0]
    for num in list:
        if num > largest:
            largest = num
    return largest
print(largest_number([2, 3, 55, 4589, .5]))



#3. Find the shortest string
#Accepts a list and returns the shortest string

def shortest_string(string_list):
    shortest = string_list[0]
    for string in string_list:
        if len(string) < len(shortest):
            shortest = string
    return shortest
# shortest_string(["apple", "banana", "pie", "orange-cranberry"])



#4. Find the longest string
#Accepts a list and returns the longest string

def longest_string(string_list):
    longest = ""
    for string in string_list:
        if len(string) > len(longest):
            longest = string
    return longest

# longest_string(["apple", "banana", "pie", "orange-cranberry"])