""" This module supposed to undestand how decorator is working.
"""

def dec_function(input_function, *args, **kwargs):
    """The decorator function.
    """
    def wrapper_function(*args, **kwargs):
        return input_function(*args, **kwargs) ** 2

    return wrapper_function

@dec_function
def function_to_be_decorated(k):
    """ Dummy function.
    """
    return k


if __name__ == "__main__":
    value = function_to_be_decorated(k=2)
    print(value)
