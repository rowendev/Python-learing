filename = input("Enter file:")
if len(filename) < 1:
    filename = "mbox-short.txt"
handle = open(filename)
mail = dict()
words = list()
maillist = list()
bigcount = None
bigmail = None
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    if words[1] in mail:
        mail[words[1]] = mail[words[1]] + 1
    else:
        mail[words[1]] = 1
        print('find new one')
    print(mail)
    #print(mail)
