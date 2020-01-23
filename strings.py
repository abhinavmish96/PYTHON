# String Formatting

# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d". Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)

name = "Abhi"
print("Hello, %s!" %name)

# To use two or more argument specifiers, use a tuple (parentheses)

# This is to print "Abhi is 23 years old."
name = "Abhi"
age = 23
print("%s is %d years old." %(name,age))