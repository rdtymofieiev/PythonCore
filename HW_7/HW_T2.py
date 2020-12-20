import re



pattern = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,16}')
password = input('Enter the password: \n')



def check_password(password):
    check = pattern.fullmatch(password)
    if not check == None:
        return 'Correct password'
    else: 
        return 'Invalid password'
    

print(check_password(password))