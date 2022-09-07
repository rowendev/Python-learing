hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
    if h > 40:
        p = 40*r+((h-40)*r*1.5)
        print("Pay:",p)
    else:
        p = h*r
        print("Pay:",p)
except:
    print("Please enter number")
