def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)  # 25
print(square.__doc__)  # Takes in a number n, returns the square of n


def sqr(n): 
    print(n)
    '''Takes in a number n, returns the square of n'''
    print(n**2)
    
print(sqr.__doc__)  # None   
# The docstring is placed incorrectly (after a print statement), so sqr.__doc__ returns None instead of the documentation text.
# Docstring must be the first statement inside a function; otherwise __doc__ returns None.

# ----------------------------------------------- Multi-line DocString ---------------==---------------------------------

def add(num1, num2):
    """
    Adds two integer numbers.

    Parameters
    ----------
    num1 : int
        First number
    num2 : int
        Second number

    Returns
    -------
    int
        Sum of num1 and num2
    """
    return num1 + num2

print(add(2, 3))  # 5