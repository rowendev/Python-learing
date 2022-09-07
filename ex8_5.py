fname = input("Enter file name: ")
fh = open(fname)
count = 0
lst = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    lst = line.split()
    count = count + 1
    print(lst[1])
print('There were',count, 'lines in the file with From as the first word')
