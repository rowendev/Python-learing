text = "X-DSPAM-Confidence:    0.8475"
num1 = text.find('0')
num2 = text.find('5',num1)
#print(num1)
#print(num2)
out = float(text[num1:num2+1])
print(out)
#out = float(num)
#print(out)
