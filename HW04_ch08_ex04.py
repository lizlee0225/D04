#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Returns true only if the first letter in the string is lowercase.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Always return true because it only checks if the letter 'c' is lowercase, which it is.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Returns false if the last letter of the string is uppercase.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Nothing is wrong.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Returns False whenever there is an uppercase letter in the string.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1('Hello'))
    print(any_lowercase2('HELLO'))
    print(any_lowercase3('pythoN'))
    print(any_lowercase5('hEllo'))

if __name__ == '__main__':
    main()
