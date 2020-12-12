""" def sum_square_even_root_odd(nums):
    new_nums = []
    for i in nums:
        if i % 2 ==0:
            i = i**2
            new_nums.append(i)
        else:
            i = i**(1/2)
            new_nums.append(i)
    return round(sum(new_nums),2)

r = [1,2,'str']

for i in r:
    while type(i) == str in r:
        r.remove(i)

print(r)

    
a = [i for i in r if type(i) == int]
print(a)

def is_square(n):
    if n % n != n:
        return False
    
digit = 26
sqrroot = digit**(1/2)
if sqrroot.is_integer():
    print('True')
num_vowels = 0
num_vowels += 1

def iq_test(numbers):
    even = [i for i in numbers if i%2==0]
    odd = [i for i in numbers if not i%2==0]
    counter = 1
    if len(even)>len(odd):
        a = [i for i, e in enumerate(numbers) if e in odd]
        counter += int(a[0])
        return counter
    else: 
        b = [i for i, e in enumerate(numbers) if e in even]
        counter += int(b[0])
        return counter

print(iq_test([3,2,3,5]))

def giq_test(numbers):
    numbers_int = [int(i) for i in numbers.replace(" ", "")]
    even = [i for i in numbers_int if i%2==0]
    odd = [i for i in numbers_int if not i%2==0]
    counter = 1
    if len(even)>len(odd):
        a = [i for i, e in enumerate(numbers_int) if e in odd]
        counter += int(a[0])
        return counter
    else: 
        b = [i for i, e in enumerate(numbers_int) if e in even]
        counter += int(b[0])
        return counter
    
    
numbers_string = ['2 4 7 8 10']
#numbers_separated = [i.replace(" ", ",").split(',') for i in numbers_string]
for i in numbers_string:
    i = i.replace(" ", ",").split(',')
    num_clear = []
    num_sep = i
    for item in num_sep:
        item = int(item)
        num_clear.append(item)
        
print(num_clear)


def iq_test(numbers):
    for i in numbers:
        i = i.replace(" ", ",").split(',')
        num_clear = []
        num_sep = i
        for item in num_sep:
            item = int(item)
            num_clear.append(item)
        
    even = [i for i in num_clear if i%2==0]
    odd = [i for i in num_clear if not i%2==0]
    counter = 1
    if len(even)>len(odd):
        a = [i for i, e in enumerate(num_clear) if e in odd]
        counter += int(a[0])
        print(a)
        return counter
    else: 
        b = [i for i, e in enumerate(num_clear) if e in even]
        counter += int(b[0])
        return counter
    



def average(n):
    result = 0
    for i in n:
    result += i
    ave_num = result / len(n)
    return ave_num

print(average([1,2,3,4,5])) """

counter = 0
while True:
    if counter<10:
        counter = counter + 1
        print(f'It works {counter} times', end=' ')
