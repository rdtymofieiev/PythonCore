import math

number1 = int(input('Please input any number '))

fact = math.factorial(number1)

print(f'The factorial of {number1} is {fact}')




number2 = int(input('Please input any number '))
factorial = 1

if number2 == 1 or number2 == 0:
    print(f'The factorial of {number2} is 1. Learn math.')
elif number2>1:
    for i in range(1,number2+1):
        factorial = factorial*i
    print(f'The factorial of {number2} is {factorial}')
else:
    print('Please input a positive number, factorial cannot be negative')
        