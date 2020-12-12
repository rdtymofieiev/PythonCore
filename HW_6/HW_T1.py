def comparison(a,b):
    """
    The function that returns the largest number of two numbers 
    a,b -- integers/bool, other objects will cause the error
    """
    return a if a>b else b

print(comparison.__doc__)