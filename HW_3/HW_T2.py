#TODO: Task 2
a=1234

#TODO: Task 2.1
digits = []

for i in str(a):
    digits.append(int(i)) 

a_spl = list(str(a))

#*: Option 1
product = int(a_spl[0])*int(a_spl[1])*int(a_spl[2])*int(a_spl[3])
print(product)

#*: Option 2
result=1
for i in a_spl:
    result = result*int(i)
print(result)

#TODO: Task 2.2
a_reverse = int(str(a)[::-1])
print(a_reverse)