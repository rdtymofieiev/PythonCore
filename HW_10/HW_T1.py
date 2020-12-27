def even_odd(number):
    if number%2 == 0:
        print("The number is even")
    elif number%2 == 1:
        print("The number is odd")

while True:
    try:
        user_age = input('How old are you? ')
        if type(user_age) != int or user_age < 0:
            raise ValueError("You entered an invalid age")
    except ValueError as e:
        print(e)
        continue
    finally: 
        even_odd(user_age)
        break
    
    
    