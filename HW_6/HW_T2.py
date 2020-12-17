import math 


def triangle(*sides):
    base = int(input(f'Please input the base of your triangle'))
    height = int(input(f'Please input the height of your triangle'))
    return (f"{base*height/2} is area of your triangle")



def rectangle(*sides):
    length = int(input(f'Please input the length of your rectangle'))
    breadth = int(input(f'Please input the breadth of your rectangle'))
    return (f"{float(breadth*length)} is area of your rectangle")



def circle(*radius):
    radius = int(input(f'Please input the radius of your circle'))
    return (f"{float(math.pi*radius**2)} is area of your circle")


if __name__ == '__main__':
    while True:
        user_choice = input('Choose the figure to calculate the area: "triangle", "rectangle", "circle" or "exit" to stop: ')

        if user_choice == 'triangle':
            print(triangle())
            break
        elif user_choice == 'rectangle':
            print(rectangle())
            break
        elif user_choice == 'circle':
            print(circle())
            break
        else:
            if user_choice.lower() == 'exit':
                print('Exit')
                break
            else:
                print(f'{user_choice} is not an option. Try again.')
    
    

