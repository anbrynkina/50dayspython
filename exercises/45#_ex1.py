"""
Create a program that:

1. Prompts the user to input a (dollar) amount.

2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.

3. Prints out the amount in euros, as shown in the screenshot below.
"""

dollar_amount = int(input("Please input a dollar amount: "))
amount_in_eur = dollar_amount * 0.95
print(amount_in_eur)

# ----- or 

rate = 0.95

dollars = float(input("How many dollars have you got? "))
euros = dollars * rate
print("The amount in euros is: ")
print(euros)

