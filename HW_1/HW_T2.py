user_var1 = int(input('Please enter random number! ')) #TODO: Task2 from PyCore 
user_var2 = int(input('Please enter random number! '))

a,b=user_var1,user_var2

def calculation(a,b):
    return (a - b, a + b, a*b, a/b, a**b)

print(calculation(a,b))