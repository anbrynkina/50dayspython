"""
Create a program that generates multiple text files by iterating over the filenames list.
The text Hello should be written inside each generated text file.
"""

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()

"""
Please download the three text files a.txt, b.txt, and c.txt from the resources. 
Then, create a program that reads each text file and prints out the content of each in the command line. 
The expected output would be like the following:
"""

abc = ["a.txt", "b.txt", "c.txt"]

for filename in abc:
    file = open(filename, 'r')
    print(file.read())