with open('romeo.txt','r') as fh:
    onelinelist = []
    for oneline in fh:
        oneline = oneline .strip()
        onelinelist.append(oneline)
        print(onelinelist)
    #for i in onelinelist:
