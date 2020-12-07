import this
import codecs


#TODO: Task 1
zen_of_python = codecs.encode(this.s, 'rot13')

#TODO: Task 1.1
#* The function is provided to split the text correctly into separate words
def clearing(text):
    text_new = text.replace(',','').replace('.','').replace('--','')
    return text_new

#* The function is provided to input the words you wanna find
#* then clean the mess in the text provided by the system 
#* finally you will get the number of word occurences in the text
def split_count(string):
    searched_words = sorted(set(input("Enter words: ").split()))
    string_cleaned = clearing(string)
    string_splitted = string_cleaned.split()
    
    search_result = []
    for i in searched_words:
        count_word = string_splitted.count(i)
        search_result.append(count_word)
    return search_result


zen_of_python_research = split_count(zen_of_python)
print(zen_of_python_research)

#TODO: Task 1.2
zen_of_python_upper = zen_of_python.upper()
print(zen_of_python_upper)

#TODO: Task 1.3
zen_of_python_replaced = zen_of_python.replace('i','&')
print(zen_of_python_replaced)


#TODO: Task 2
a=1234

#TODO: Task 2.1
digits = []

for i in str(a):
    digits.append(int(i)) 

a_spl = list(str(a))

#*: Option 1
product = int(a_spl[0])*int(a_spl[1])*int(a_spl[2])*int(a_spl[3])
print(product)

#*: Option 2
result=1
for i in a_spl:
    result = result*int(i)
print(result)

#TODO: Task 2.2
a_reverse = int(str(a)[::-1])
print(a_reverse)

#TODO: Task 2.3
a = 2
b = 3
print(a,b)
a,b=b,a
print(a,b)


