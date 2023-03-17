"""
Please download the members.txt file from the resources of this article.
Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
Then, the member is added to members.txt. In this case, the text file content would be:

John Smith
Sen Lakmi
Sono Octonot
Solomon Right
"""
member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()
