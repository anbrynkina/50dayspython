"""
We have the same list:

ranking = ['John', 'Sen', 'Lisa']

This time you need to create a program that:

1. Contains the above list.

2 Prompts the user to input the person's name.

3. Returns the rank that person has.
"""

ranking = ['John', 'Sen', 'Lisa']
print(ranking)
name = input("Please write a name from the list: ")
# index() method returns the index of the specified element in the list
index = ranking.index(name)
index = int(index) + 1
print(index)

# or -----

ranking = ['John', 'Sen', 'Lisa']
name = input("Enter a name: ")
rank = ranking.index(name) + 1
print(rank)