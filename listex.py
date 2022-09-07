friend = ['john','jack','amy']

for i in range(len(friend)):
    print('hi,',friend[i])

numlist = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done':
        break;
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print('the average is:',average)
