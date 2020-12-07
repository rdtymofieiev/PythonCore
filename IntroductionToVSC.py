user_name = input('What is your name? ')
user_age = int(input('How old are you? '))
user_email = input('What is your email address? ')
print(f'Hello {user_name}, you are {user_age} years old, I will write you soon at {user_email}.') #TODO: Task1 from PyCore 

user_var1 = int(input('Please enter random number! ')) #TODO: Task2 from PyCore 
user_var2 = int(input('Please enter random number! '))
a,b=user_var1,user_var2

def calculation(a,b):
    return (a - b, a + b, a*b, a/b, a**b)

print(calculation(a,b))