# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("Hello " + user_name)

name = input("What is your name? ")
hello_name(name)

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    x = 0
    while x < 100:
        x += 1
        if x%2 != 0:
            print(x)
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_number_in_list(a_list):
    i = 0
    stored = 0
    while i < len(a_list):
        x = a_list[i]
        if a_list[i] > stored:
            stored = x
        print(x)
        i += 1
    print("The largest number in the list is " + str(stored))

myList = [54, 23, 78, 11, 102, 55, 54, 53, 54, 54]
max_number_in_list(myList)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if (a_year % 4 == 0) & (a_year % 100 != 0):
        print("Yes, the year " + str(a_year) + " is a leap year")
        return True
    elif (a_year % 400 == 0) & (a_year % 100 == 0):
        print("Yes, the year " + str(a_year) + " is a leap year")
        return True
    else:
        print("No, the year " + str(a_year) + " is not a leap year")
        return False

x = int(input("What year would you like to check? "))
is_leap_year(x)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    i = 0
    stored = 0
    while i < len(a_list):
        x = a_list[i]
        if a_list[i] > stored:
            stored = x
        else:
            print("The list is not in order")
            break
        i += 1

myList = [2,3,4,5,6,7]
is_consecutive(myList)