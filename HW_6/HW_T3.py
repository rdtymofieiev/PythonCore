def count_char(string):
    """
    The function counts the number of characters, excluding whitespaces
    """
    return len(string.replace(" ",""))

print(count_char("Hello world"))
print(count_char.__doc__)