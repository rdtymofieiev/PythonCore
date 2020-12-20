import random



start,end = 1,101
number_to_guess = random.randint(start,end-1)
player_name = str(input('What is your name, lad? '))
print(number_to_guess)
guesses_taken = 1


while True:
    try:
        player_choice = int(input(f'What number are we thinking of from {start} to {end}? Try your best: '))
        break
    except ValueError:
        print("Are you numb? You must guess the number, not the name of stupidest gambler")  
        continue


while True: 
    try:       
        while not player_choice == number_to_guess:
            guesses_taken +=1
            if player_choice>number_to_guess:
                print('Too much! The number is smaller.')
                player_choice = int(input('What number are we thinking of? Try your best '))
            elif player_choice<number_to_guess:
                print('You are too shy! The number is bigger.')
                player_choice = int(input('What number are we thinking of? Try your best '))
        break
    except ValueError:
        print("Are you numb? You must guess the number, not the name of stupidest gambler")  
        continue

        
if player_choice == number_to_guess:
    if guesses_taken==1:
        print(f'{player_name.upper()}, OMG YOU ARE SO LUCKY!!! \nMaybe you cheated? Nevermind, just a silly joke:) \nCongratulations!')
    else:
        print(f'{player_name}, it takes {guesses_taken} attempts for you to guess. \nCongratulations!')

