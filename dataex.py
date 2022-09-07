a = 'banana'

print('the third word is:',a[3])

print('length is:',len(a))

index = 0
while index < len(a):
    letter = a[index]
    print(index + 1,'word is',letter)
    index = index + 1

for letter in a:
    print(letter)

count = 0
for letter in a:
    if letter == 'a':
        count = count + 1
print(count)

b = 'I AM HANDSOME'
print('i am handsome'.lower())
print(b.capitalize())
nstr = b.replace('I','HE')
print(nstr)

pos = b.find('HAND')
print('HAND is in position',pos)

print(b[0:2])
print(b[2:4])
print(b[5:])

foundletter = input('Enter what u want2 find:')
if foundletter in b:
    print('found!')
else:
    print('nothing!')
