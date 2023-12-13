""" 
Practice Question 1: Age Verifier

Task:

Write a function age_verifier that continuously asks the user for 
their age until they provide a valid age (a number from 1 to 120). 
Once a valid age is provided, the function should print a message confirming the age.
"""

def age_verifier():
    flag = True
    while flag: 
        try: 
            user_input = int(input('Enter a valid age between 1 and 120: '))
            if user_input < 1 or user_input > 120:
                print('Invalid age. Please try again.')
                continue
            print(f'Your age is {user_input}')
            flag = False
        except ValueError:
            print('Invalid age. Please try again.')
            continue
