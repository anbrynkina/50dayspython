"""
names = ["john smith", "jay santi", "eva kuki"]

Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.

The output of your code should be as below:

['John Smith', 'Jay Santi', 'Eva Kuki']
"""

names = ["john smith", "jay santi", "eva kuki"]
capitalized_names = [i.title() for i in names]
print(capitalized_names)

"""
usernames = ["john 1990", "alberta1970", "magnola2000"]

Extend the code above so the code prints out a list containing the number of characters for each username.

The output of your code should be as below:
"""

usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames_len = [len(username) for username in usernames]
print(usernames_len)

"""
user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out a list containing the same items as floats.
The output of your code should be as below:
[10.0, 19.1, 20.0]
"""

user_entries = ['10', '19.1', '20']
float_user_entries = [float(i) for i in user_entries]
print(float_user_entries)

"""
user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out the sum of the numbers.

The output of your code should be as below:

49.1
Hint: Use the sum() function. The function gets a list of numbers as input and produces the sum of all numbers. 
For more info, try help(sum).
"""

user_entries = ['10', '19.1', '20']
float_user_entries = [float(i) for i in user_entries]
print(sum(float_user_entries))