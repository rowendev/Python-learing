c = {'a':10,'b':22,'c':1}

print(sorted( [(v,k) for k,v in c.items() ] , reverse=True))
