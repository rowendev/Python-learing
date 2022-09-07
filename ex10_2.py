filename = input("Enter file:")
if len(filename) < 1:
    filename = "mbox-short.txt"
handle = open(filename)
words = list()
mail = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5].split(':')
    #print(words[5] , time[0])
    mail[time[0]] = mail.get(time[0],0) + 1
    #print(mail)
for a,b in sorted( [(hour,tim) for hour,tim in mail.items() ] ):
    print(a, b)
#print( sorted( [(hour,tim) for hour,tim in mail.items() ] ) )
