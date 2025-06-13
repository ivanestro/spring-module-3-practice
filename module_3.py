import math
import random



# Question 1
"""
Write a program that generates two random numbers between 0 and 100

args
number = random.randint(0, 100)
number2 = random.randint(0, 100)

return
Your first number is less than your second number generated 18, 54
"""
number = random.randint(0, 100)
number2 = random.randint(0, 100)
print("Question 1 comparing two numbers and is lesser")
if number < number2:
    print(f"Your first number is less than your second number generated {number}, {number2}")

elif number2 < number:
    print(f"Your second number is less than your first number generated {number2}, {number}")

else:
    print("Same number")

# Question 2
"""
Write a program takes float as input then computes and outputs the cube of a number

args
cube = math.pow(cube, 3)

return
Please Enter a number and will cube it 5
Your number is 125.0
"""
print("\nWelcome to Question 2 cubing a number")
cube = float(input("Please Enter a number and will cube it "))
cube = math.pow(cube, 3)
print(f"Your number is {cube}")

# Question 3
"""
Write a program that computes area and circumference

args
area =  3.14 * (2 ** area)
circumference = (2 * 3.14) * circumference

return
Your Area is: 50.24
Your Circumference is: 25.12
"""
print("\nWelcome to Question 3 Calculator of Area and Circumference")

area = float(input("Enter your radius for your area: "))
circumference = float((input("Enter your radius for circumference: ")))

area =  3.14 * (2 ** area)
circumference = (2 * 3.14) * circumference

print(f"Your Area is: {area}")
print(f"Your Circumference is: {circumference}")

# Question 4
"""
Write a program to generate 5 random numbers on a list between 60 and 100

args
random_number =[]
number = random.randint(60, 100)
random_number.append(random_number)

return
63
64
99
86
94
"""
print("\nWelcome to Question 4 generating 5 random int between 60 and 100")
random_number =[]

for i in range(0, 5):
    number = random.randint(60, 100)
    random_number.append(random_number)
    print(number)

# Question 5
"""
Write a program to generate 3 random number and calculates average 
prints the result to one decimal place.

args
number1 = random.randint(0, 50)
number2 = random.randint(0, 50)
number3 = random.randint(0, 50)

return
Question 5 Generates 3 random number and outputs average
Your 3 random numbers are: (5, 27, 25)
Your average for the three numbers is 19.0
"""
print("\nQuestion 5 Generates 3 random number and outputs average")
number1 = random.randint(0, 50)
number2 = random.randint(0, 50)
number3 = random.randint(0, 50)

average = (number1 + number2 + number3) / 3

print(f"Your 3 random numbers are: {number1, number2, number3}")
print(f"Your average for the three numbers is {average}")

# Question 6
"""
Write a program representing number of hits and number of bats scored

args


return

"""
print("\nQuestion 6 Number of hits | Number of misses from a baseball")

number_of_hits = float(input("Enter your number of hits "))
number_of_misses = float(input("Enter your number of misses "))
hit_rate = number_of_hits / number_of_misses
print(f"Your hit rate is: %{hit_rate:.2f}")

if hit_rate  >= .300:
    print("You Are Eligible For The All Stars Game")

else:
    print("You are not qualified for All Stars Game")

# Question 7
"""
Write a program to enter a valid single letter.

args
letter = ''

return

Question 7 Write a single character as input if it is valid length of character
Please Enter A Valid Single Letter Character a
You have entered a valid letter: a
"""
print("\nQuestion 7 Write a single character as input if it is valid length of character")

letter = ''

letter = input("Please Enter A Valid Single Letter Character ")
if len(letter) == 1:
    print(f"You have entered a valid letter: {letter}")
elif len(letter) >= 2:
    print("You have inputted an invalid letter")
else:
    print("EXIT")

# Question 8
"""
Write a program that reads the sentence as a period, question mark, exclamation point etc
Based on other expressions at the end of the sentence.

args
sentence = ''
sentence.split()

return
Your sentence ends with a period .
Your sentence ends with a exclamatory !
Your sentence ends with a question mark ?
other
"""
print("\nQuestion 8 Write a Sentence and the program will know at the end of the sentence.")

sentence = ''
sentence.split() # If used with spaces to prevent issues.

sentence = input("Write a sentence or a simple declarative, interrogative, exclamatory or other ")
if sentence.endswith('.'):
    print("Your sentence ends with a period .")

elif sentence.endswith('!'):
    print("Your sentence ends with a exclamatory !")

elif sentence.endswith('?'):
    print("Your sentence ends with a question mark ?")

else:
    print("other")

# Question 9
"""
Write a program if it is an email address based on the @ character

args
email = ''

return
It is an email
It is not an email
"""
print("\nQuestion 9: Write if it is an email address and system will check")
email = ''
email = input("Write: ")
if '@' in email:
    print("It is an email ")

else:
    print("It is not an email ")

# Question 10
"""
Write a program if both password match

args
password1 = input("Enter your password ")
password2 = input("Enter your password again ")

return
You are registered as a new user
Sorry, there is a typo in your password
"""
print("\n Question 10: Write if both password match.")

password1 = input("Enter your password ")
password2 = input("Enter your password again ")

if password1 == password2:
    print("You are registered as a new user")

else:
    print("Sorry, there is a typo in your password")

# Question 11
"""
Write a program length 6 to 10 then output welcome as a user ID

args
len.(userID)

return
Welcome, {userID}
Sorry, user ID invalid
"""
print("\n Question 11: Length Character 6 to 10 for user ID")

userID =  input("Please enter a user ID ")


if len(userID) >= 6:
    print(f"Welcome, {userID}")

elif len(userID) == 10:
    print(f"Welcome {userID}")

else:
    print("Sorry, user ID invalid")

# Question 12
"""
Write a program for a user to enter a web address

args
web_address = ''

return
Enter a web address
It is a government web address

"""
web_address = ''

web_address = input("Enter a web address ")

if web_address.endswith('gov'):
    print("It is a government web address.")

elif web_address.endswith('edu'):
    print("It is a university web address")

elif web_address.endswith('com'):
    print("It is a business web address")

elif web_address.endswith('org'):
    print("It is an organization web address")

else:

    print("A web address for another entity")

# Question 13
print("\n Question 13: Enter A Temperature from -4 to 109")
temperature = int(input("What is the Temperature? "))

if  temperature == -5 or temperature == 110:
    print("That temperature is outside the valid range")

elif temperature >= 90:
    print("It is probably summer")

elif temperature >= 70:
    print("It is probably spring")

elif temperature >= 50:
    print("It is probably fall")

elif temperature == 50:
    print("It is probably winter")

else:
    print("Thank you for using the Temperature program.")


# Question 14