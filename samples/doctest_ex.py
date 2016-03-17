def my_function(a, b):
    '''
    >>> my_function(3,4)
    13
    >>> my_function(5,5)
    25
    '''
    return a * b

def main():
    print(my_function(3,6))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
