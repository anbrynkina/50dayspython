"""Create a program that prompts the user to input their name once.
Then, the program repeatedly prints out the name with the first letter capitalized."""

name = input("Please enter your name: ")

while True:
    print(name.capitalize())
