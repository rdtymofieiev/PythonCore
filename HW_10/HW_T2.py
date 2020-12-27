week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
try:
    day = int(input('Enter the number of the dat (1-7): '))
    #if day > 7:
        #raise ValueError('You have only 7 days in week')
    print(f'{day} is {week[day-1]}')
except IndexError as e:
    print("There are no such day in the week: ",e)
except ValueError as e:
    print("Invalid input for the number of the day of the week")