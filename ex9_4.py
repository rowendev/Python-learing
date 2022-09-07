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
    #print(words)
    #print(words[1])
#    if not words[1] in maillist: #get the mail account
#        maillist.append(words[1])
#    print(maillist)
    mail[words[1]] = mail.get(words[1],0) + 1
    #print(mail)
for word,count in mail.items():
    if bigcount is None or count > bigcount:
        bigmail = word
        bigcount = count
print(bigmail, bigcount)
