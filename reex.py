import re
count = 0
sum = 0
hand = open('regex_sum_1529691.txt')

for line in hand:
    line = line.strip()
    #word = line.split()
    y = re.findall('^.*\d+?',line)
    if len(y) != 1 : continue
    #print('Find number!',y[0])

    if len(y[0]) > 1:
        ll = y[0].split()

        for l in ll:
            l = l.strip()
            y1 = re.findall('^.*[0-9]+',l)

            if len(y1) != 1 : continue

            if '.' in y1[0] :
                #print('\nno!!!!\n')
                spe = y1[0].split('.')
                for ss in spe:
                    #print(ss)
                    s = re.findall('[0-9]+',ss)
                    if len(s) != 1 : continue
                    count = count + 1
                    #print(s[0],count,'numbers')
                    sum = sum + int(s[0])
            else:
                count = count + 1
                #print(y1[0],count,'numbers')
                #y2 = re.findall('^.*[0-9]+',y1[0])
                #print('special:',y2[0])
                sum = sum + int(y1[0])
print('sum',sum)
