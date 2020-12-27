

while True:
    
    try:
        user_input = int(input("Please enter your number"))
        if user_input % 2 == 0:
            print(f'{user_input} is even')
        elif user_input % 2 == 1:
            print(f'{user_input} is odd')
        break
    except ValueError as e:
        print('Please enter correct value')
        continue
