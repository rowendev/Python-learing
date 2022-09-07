fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line.rstrip())#[val1+1:])
    val = line.find(':')
    print(line[val+2:].rstrip())
    val1 = float(line[val+2:])
    print(val1)
    total = total + val1
    count = count +1
    print(total,count)
print('Average spam confidence:',total/count)
