"""
Please download the essay.txt file from the resources of this article.
Then, create a program that reads that file and prints out its text.
The first letter of each word in the output should be uppercase.
"""

file = open("essay.txt", 'r')
content = file.read()
print(content.title())

"""
Write a program that reads the essay.txt file 
and returns the number of characters contained in the file
"""

file = open("essay.txt", 'r')
content = file.read()
print(len(content.title()))


# or

file = open("essay.txt", 'r')
content = file.read()

nr_chars = len(content)
print(nr_chars)