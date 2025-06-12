# Module 3 Practice Problems

## Author

Ivan Estropigan

- Question 1

Write a program that generates two random numbers between 0 and 100 and prints the smaller of the two numbers.

- Question 2

Write a program that takes a float as an input, then computes and outputs the cube of that number using the pow method of the math module.

- Question 3

Write a program that reads from the keyboard the radius of a circle. Calculate and output the area and the circumference of that circle. You can use the following formulas:

```cs
A = pie r^2
C = 2pie r
```

- Question 4

Write a program that generates five random integers between 60 and 100 and calculates the smallest of the five numbers.

- Question 5

Write a program that generates three random integers between 0 and 50, calculates the average, and prints the result to one decimal place.

- Question 6

Write a program that takes two integers as input from the keyboard, representing the number of hits and the number of at-bats for a batter. Then calculate the batter’s hitting percentage and check if the hitting percentage is above .300. If it is, output that the player is eligible for the All Stars Game; otherwise, output that the player is not eligible.

- Question 7

Write a program that reads a single char as an input from the keyboard and outputs whether it is a valid character to start a variable identifier.

- Question 8

Write a program that reads a sentence from the keyboard. Depending on the last character of the sentence, print a message identifying the sentence as declarative (ends with a period), interrogative (ends with a question mark), exclamatory (ends with an exclamation point), or other.

- Question 9

An email address contains the @ character. Write a program that takes a word from the keyboard and outputs whether it is an email address based on the presence of the @ character. Do not worry about what else is in the word.

- Question 10

Write a program that takes two words as input from the keyboard, representing a password and the same password again. (Often, websites ask users to type their password twice when they register to make sure there was no typo the first time around.) Your program should do the following:
    - if both passwords match, then output "You are now registered as a new user"
    - otherwise, output "Sorry, there is a typo in your password"

- Question 11

Write a program that takes a word as input from the keyboard, representing a user ID. (Often, websites place constraints on user IDs.) Your program should do the following:
    - if the user ID contains between 6 and 10 characters inclusive, then output "Welcome, barbara" (assuming barbara is the user ID entered)
    - otherwise, output "Sorry, user ID invalid"

- Question 12

Write a program that reads a web address (for instance, www.yahoo.com) from the keyboard and outputs whether this web address is for a government, a university, a business, an organization, or another entity.
    - If the web address ends with gov, it is a government web address.
    - If the web address ends with edu, it is a university web address.
    - If the web address ends with com, it is a business web address.
    - If the web address ends with org, it is an organization web address.
    - Otherwise, it is a web address for another entity.

- Question 13

Write a program that reads a temperature as a whole number from the keyboard and outputs a "probable" season (winter, spring, summer, or fall) depending on the temperature.
    - If the temperature is greater than or equal to 90, it is probably summer.
    - If the temperature is greater than or equal to 70 and less than 90, it is probably spring.
    - If the temperature is greater than or equal to 50 and less than 70, it is probably fall.
    - If the temperature is less than 50, it is probably winter.
    - If the temperature is greater than 110 or less than −5, then you should output that the temperature entered is outside the valid range.

- Question 14

Write a program that takes a String as input from the keyboard, representing a year. Your program should do the following:
    - If the year entered has two characters, convert it to an integer, add 2000 to it, and output it.
    - If the year entered has four characters, just convert it to an integer and output it.
    - If the year entered has neither two nor four characters, output that the year is not valid.

- Question 15

Write a program that takes two words as input from the keyboard, representing a user ID and a password. Your program should do the following:
    - If the user ID and the password match "admin" and "open," respectively, then output "Welcome."
    - If the user ID matches "admin" and the password does not match "open," output "Wrong password."
    - If the password matches "open" and the user ID does not match "admin," output "Wrong user ID."
    - Otherwise, output "Sorry, wrong ID and password."

- Question 16

Write a program that prompts the user for a value greater than 10 as an input (you should loop until the user enters a valid value) and finds the square root of that number and the square root of the result, and continues to find the square root of the result until you reach a number that is smaller than 1.01. The program should output how many times the square root operation was performed.

- Question 17

Write a program that expects a word containing the @ character as an input. If the word does not contain an @ character, then your program should keep prompting the user for a word. When the user types in a word containing an @ character, the program should simply print the word and terminate.

- Question 18

Write a program that reads float values from a file named input.txt and outputs the average.

- Question 19

Write a program that uses a for loop to output the sum of all the integers between 10 and 20, inclusive, that is, 10 + 11 +12 + ... + 19 + 20.

- Question 20

Write a program that uses a for loop to output the product of all the integers between 3 and 7, inclusive, that is, 3 * 4 * 5 * 6 * 7.

- Question 21

Write a program that uses a for loop to count how many multiples of 7 are between 33 and 97, inclusive.



- Question 22

Write a program that reads an integer value from the user and outputs Hello World the number of times enter by the user. Verify that the user has entered an integer. If the input is 3, the output will be Hello World printed three times.

- Question 23

Write a program that takes a word as an input from the keyboard and outputs each character in the word, separated by a space.

- Question 24

Write a program that takes an integer value as an input from the keyboard and outputs the factorial of that number; the factorial of an integer n is n * (n − 1) * (n − 2) * ... * 3 * 2 * 1. For instance, the factorial of 4 is 4 * 3 * 2 * 1, or 24.

- Question 25

Using a loop, write a program that reads 10 integer values from the keyboard and outputs the minimum value of all the values entered.

- Question 26

Write a program that inputs a word representing a binary number (0s and 1s). First, your program should verify that it is indeed a binary number, that is, the number contains only 0s and 1s. If that is not the case, your program should print a message that the number is not a valid binary number. Then, your program should count how many 1s are in that word and output the count.

- Question 27

Create a copy of the previous problem and update it with the following modification: If the word does not represent a valid binary number, the program should keep prompting the user for a new word until a word representing a valid binary number is input by the user.

- Question 28

Write a program that inputs a word representing a binary number (0s and 1s). First, your program should check that it is indeed a binary number, that is, the number contains only 0s and 1s. If that is not the case, your program should output that the number is not a valid binary number. If that word contains exactly two 1s, your program should output that that word is "accepted," otherwise that it is "rejected."

- Question 29

Create a copy of the previous problem and update it with the following modification: If the word does not represent a valid binary number, the program should keep prompting the user for a new word until a word representing a valid binary number is input by the user.

- Question 30

Write a program that inputs a word representing a binary number (0s and 1s). First, your program should check that it is indeed a binary number, that is, that it contains only 0s and 1s. If that is not the case, your program should output that the number is not a valid binary number. If that word contains at least three consecutive 1s, your program should output that that word is "accepted," otherwise that it is "rejected."

- Question 31

Write a program that inputs 7 float values from a file dja.txt that represent the Dow Jones Average for 7 days. Your program should output the lowest value for those 7 days and the number of the day on which the lowest value occurred. For this program, instead of setting the initial minimum value to the first value in the file, use the maximum value for a float (sys.float_info.max). Be sure to handle the case of the file being empty.

- Question 32

Write a program that takes website names as keyboard input until the user types the word stop and counts how many of the website names are commercial website names (i.e., end with .com), then outputs that count. The input of the word stop should be case insensitive.

- Question 33

Using a loop, write a program that takes 10 values representing exam grades (between 0 and 100) from the keyboard and outputs the minimum value, maximum value, and average value of all the values entered. Your program should not accept values less than 0 or greater than 100.

- Question 34

Write a program that takes an email address as an input from the keyboard and, using a loop, steps through every character looking for an @ sign. If the email address has exactly one @ character, then print a message that the email address is valid; otherwise, print a message that it is invalid.

- Question 35

Write a program that takes a user ID as an input from the keyboard and steps through every character, counting how many digits are in the user ID; if there are exactly two digits, output that the user ID is valid, otherwise that it is invalid.

- Question 36

Write a program that takes an integer value as an input and converts that value to its binary representation; for instance, if the user inputs 17, then the output will be 10001.

- Question 37

Write a program that takes a word representing a binary number (0s and 1s) as an input and converts it to its decimal representation; for instance, if the user inputs 101, then the output will be 5; you can assume that the input is guaranteed to contain only 0s and 1s.

- Question 38

Write a program that takes a sentence as an input and checks whether that sentence is a palindrome. A palindrome is a word, phrase, or sentence that is symmetrical; that is, it is spelled the same forward and backward. Examples are "otto," "mom," and "Able was I ere I saw Elba." Your program should be case insensitive; that is, "Otto" should also be counted as a palindrome.

- Question 39

Write a program that prints the product of all the elements in an List of integers.

- Question 40

Write a program that multiplies by 2 all the elements of a List of floats.

- Question 41

Write a program that prints the percentage of elements greater than or equal to 90 in a List of integers.

- Question 42

Write a program that prints the difference between the largest and smallest elements in a List of floats.

- Question 43

Write a program that prints the sum of all the elements of a List of integers that have an odd index.

- Question 44

Write a program that prints the percentage of the number of elements that have the value true in a List of booleans.

- Question 45

Write a program that prints true if a List of strings contains the string "Hello"; false otherwise.

- Question 46

Write a program that prints all the elements of a List of strings in reverse order.

- Question 47

Write a program that prints a List composed of all the elements in a List of strings in reverse order.

- Question 48

Write a program that reads a string as input and prints a list containing the characters of the string.

- Question 49

Code a program that creates a List of booleans based on a List of integers, assigning true for any element of the List greater than or equal to 100; and false otherwise.

- Question 50

Write a program that reads a file and writes a copy of the file to another file with line numbers inserted.

- Question 51

In Internet programming, programmers receive parameters via a query string, which looks like a string with fields separated by the "&" character. Each field typically has a metadata part that identifies the data followed by an equals sign and then the data. An example of a query string is: first=Mike&last=Jones&id=mike1&password=hello

Read and parse a query string and output each field on a different line after replacing the equal sign with a colon followed by a space. For example, for the preceding sample query string, the output should be:

```cs
first: Mike
last: Jones
id: mike1
password: hello
```

- Question 52

Write a program that reads a file that contains only one line; output all the characters, one character per line.

- Question 53

Write a program that reads a file and counts how many lines it contains.

- Question 54

Write a program that reads a text file that contains a grade (for instance, 87) on each line. Calculate and print the average of the grades.

- Question 55

Write a program that reads a text file and writes to a file every line of the file separated by a blank line.

- Question 56

Often websites display the visitor count ("You are visitor number 5246"). Write a program that reads a file that holds the visitor count, outputs it, and updates the file, incrementing the visitor count by 1.

[EOF]