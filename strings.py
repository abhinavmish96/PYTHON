# String Formatting

# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d". Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)

name = "Abhi"
print("Hello, %s!" %name)

# To use two or more argument specifiers, use a tuple (parentheses)

# This is to print "Abhi is 23 years old."
name = "Abhi"
age = 23
print("%s is %d years old." %(name,age))

# Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# Strings are bits of text. They can be defined as anything between quotes

astring1 = "Hello World!"
astring2 = 'Hello World!'

# As you can see, the first thing you learned was printing a simple sentence. This sentence was stored by Python as a string. However, instead of immediately printing strings out, we will explore the various things you can do to them. You can also use single quotes to assign a string. However, you will face problems if the value to be assigned itself contains single quotes.For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.

# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.

# But why didn't it print out 5? Isn't "o" the fifth character in the string? To make things more simple, Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.

astring = "Hello World!"
print(astring.index("o"))

# For those of you using silly fonts, that is a lowercase L, not a number one. This counts the number of l's in the string. Therefore, it should print 3

astring = "Hello World!"
print(astring.count("l"))