# Arithmetic Operators

number = 1 + 2 * 3/10
print(number)


# Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder

reminder = 11%3
print(reminder)

# Using two multiplication symbols makes a power relationship

squared = 7 ** 2
cubed = 4 ** 3
print(squared)
print(cubed)

# Using Operators with Strings

# Python supports concatenating strings using the addition operator

hw = "Hello" + " " + "World"
print(hw)

# Python also supports multiplying strings to form a string with a repeating sequence:

lotsOfHellos = "hello" * 10
print(lotsOfHellos)

# Using Operators with Lists

# Lists can be joined with the addition operators

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers =  odd_numbers + even_numbers
print(all_numbers)

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator

print([1,2,3]*3)