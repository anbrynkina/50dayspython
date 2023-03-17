"""
The zip() function in Python is used to combine two or more iterables
e.g., lists, tuples, or strings) into a single iterable.
The resulting iterable contains tuples where the i-th tuple contains
the i-th element from each of the input iterables.
"""

contents = ["You can write to each file separately",
           "And also using a zip function you can combine two or more iterables",
           "Into a single iterable"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"..app1\files\{filename}", 'w')
    file.write(content)




