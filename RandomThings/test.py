

while True:
    try:
        a, b = [int(x) for x in input("Enter two values\n").split(', ')] 
        print(a/b)
        break
    except ZeroDivisionError as e:
        print('Please do not input zero values')
    except ValueError as e:
        print('Please do not input string for division')
    finally
        print('The code finished successfully')
