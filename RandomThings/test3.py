while True:
    try:
        a, b = [int(x) for x in input("Enter two values\n").split(', ')] 
        print(a/b)
        
    except ZeroDivisionError as e:
        print('Please do not input zero values')
        continue
    except IndexError as e:
        print('Please enter only two numbers')    
    except ValueError as e:
        print('Please the correct quantity of numbers')  
    else:
        print('Else block')
    finally:
        print('The code finished successfully')
    break
