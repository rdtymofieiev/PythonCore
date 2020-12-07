start_number = 0
finish_number = 100

while start_number<finish_number:
    if start_number % 2 == 0:
        print(start_number)  
    start_number += 1
else: 
    print('THE END')

for i in range(0, 101, 2): 
	print(i) 
 

print(list(range(0, 101, 2)))