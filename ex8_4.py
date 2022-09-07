fname = input("Enter file name: ")
fh = open(fname)
lst = list()
word = list()

for line in fh:
    line = line.rstrip()
    lst = line.split()
    for line1 in lst:
        if not line1 in word:
            word.append(line1)
word.sort()
print(word)
