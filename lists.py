myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[0]) # prints 1
print(myList[1]) # prints 2
print(myList[2]) # prints 3

for x in myList:
    print(myList[x])


# Accessing an index which does not exist generates an exception (an error)

mylist = [1,2,3]
print(mylist[10])