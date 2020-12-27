def double_char(s):
    string_double =''
    for i in s:
        string_double+=i*2 
    return string_double



def double_char1(s):
    return ''.join(i*2 for i in s)

