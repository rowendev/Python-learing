smallest = None
largest = None

while True:
    num1 = input('Enter a number:')

    if num1 == 'done':
        break
    try:
        num = int(num1)
        if smallest is None:
           smallest = num
           largest = num
           #print('smallest:',smallest,'largest:',largest)
        elif num < smallest:
           smallest = num
           #print('smallest:',smallest,'largest:',largest)
        elif num > largest:
           largest = num
           #print('smallest:',smallest,'largest:',largest)
        #else:
           #print('smallest:',smallest,'largest:',largest)
    except:
        print('Invalid input')

print('Maximum is', largest)
print('Minimum is', smallest)
