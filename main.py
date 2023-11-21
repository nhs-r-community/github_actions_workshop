"""
This is our main python script file. This defines our functions and runs the code. Nothing fancy!
"""


def example_add(num_1: int | float, num_2: int | float) -> int | float:
    """
    Adds two numbers together.

    Parameters
    ----------
    num_1 : int | float
        First number you want to add together.
    num_2 : int | float
        Second number you want to add together

    Returns
    -------
    int | float
        Sum of num_1 and num_2
    """
    return num_1 + num_2

# TODO - Implement function and tests
def example_bad_add(num_1: int | float, num_2: int | float) -> int | float:
    """
    Badly adds two numbers together.

    Parameters
    ----------
    num_1 : int | float
        First number you want to add together.
    num_2 : int | float
        Second number you want to add together

    Returns
    -------
    int | float
        Sum of num_1 and num_2... and + 1
    """
    return num_1 + num_2 + 1
