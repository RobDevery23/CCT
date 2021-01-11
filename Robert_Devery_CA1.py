# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:24:03 2020

@author: robde
"""
# 1. Title.
print("Stage name generator!")

# 2. Import random module
import random

# 3. Ask the user how many names they want to change.
#    Make sure they enter a positive number.
while True:
    try:
        no_of_names = int(input("Enter the number of names you want to change: "))
    except ValueError:
        print("Please enter a whole number.")
        continue
    if no_of_names <= 0:
        print("Please enter a positive number.")
    else:
        break
print("\n")

# 4. Allow user to input as many regular names as they defined in the first step.
#    Make sure they enter the correct format i.e. firstname lastname
first_names = []
last_names = []

for x in range(0, no_of_names): 
    while True:
        try:
            first_name = (input("Enter first name: "))
        except ValueError:
            continue
        if first_name.isalpha():
            break
        else:
            print("Only enter a first name here. No numbers or blank spaces. Please try again.")

    first_names.append(first_name.title())
    
    while True:
        try:
            last_name = (input("Enter last name: "))
        except ValueError:
            continue
        if last_name.isalpha():
            break
        else:
            print("Only enter a last name here. No numbers or blank spaces. Please try again.")

    last_names.append(last_name.title())
    
print("\n")
print("\n")

# 5. Make a list of choices for the random function to choose from.
choices = ("Michael", "Jim", "Dwight", "Pam", "Angela", "Andy", "Phyllis", "Oscar", "Kevin", "Meredith", "Stanley", "Kelly", "Ryan")

# 6. Make a list of initials for the stage name
initials = [x[0] for x in first_names]

# 7. Generate stage names using user generated names lists.
stage_names = []

for init, f_name, l_name, choice in zip(initials, first_names, last_names, choices):
    stage_name = ('{} {} {} {} {}'.format(init + ".", random.choice(choices), l_name.upper() , f_name.lower(), random.choice(choices)))
    stage_names.append(stage_name)

# 8. Combine lists of first names and last names into a single list
full_names = [f + " " + l for f, l in zip(first_names, last_names)]

# 9. Print the original names and the generated stage names.
print("Regular names - ", full_names)
print("\n")
print("Stage names - ", stage_names)
