def computepay(h, r):
    if h > 40:
        pay = float(40*r+((h-40)*r*1.5))
    else:
        pay = h*r
    return pay
try:
    hrs = input("Enter Hours:")
    rate = input("Enter rate:")
    h1 = float(hrs)
    r1 = float(rate)
    p = computepay(h1, r1)
    print("Pay",p )
except:
    print("Please Enter the right number")
