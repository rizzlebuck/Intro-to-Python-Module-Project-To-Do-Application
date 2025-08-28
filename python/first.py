# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)

#Write a function that removes the spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(" ", "")


