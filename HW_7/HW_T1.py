from geometry import area

user_choice = int(input("Hi, user, you can calculate the area of three types of figures, \n Type 1 for rectangle \n Type 2 for triangle \n Type 3 for circle:\n"))

if user_choice == 1:
    a = int(input("Input the length of your rectangle"))
    b = int(input("Input the breadth of your rectangle"))
    print(f'Area of the rectangle equals {area.rectangle(a,b)}')
elif user_choice == 2:
    a = int(input("Input the length of base side of the triangle"))
    h = int(input("Input the height of the triangle"))
    print(f'Area of the rectangle equals {area.triangle(a,h)}')
elif user_choice == 3:
    radius = int(input("Input the radius of the circle"))
    print(f'Area of the rectangle equals {area.circle(radius)}')
else:
    print("Something went wrong! Try again")