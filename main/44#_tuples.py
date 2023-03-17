filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

# replace first appearance of '.' to '-' for all files in the list
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

