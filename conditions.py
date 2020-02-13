# Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated

# Notice that variable assignment is done using a single equals operator "=", whereas comparison between two variables is done using the double equals operator "==". The "not equals" operator is marked as "!=".

x = 2
print( x == 2)
print( x == 3)
print(x < 3)

# Boolean operators; The "and" and "or" boolean operators allow building complex boolean expressions, for example

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The "in" operator

# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. Notice that code blocks do not need any termination.

# Here is an example for using Python's "if" statement using code blocks:

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# For example:

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")