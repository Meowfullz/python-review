# The print function prints its parameter to standard out
# and appends a line separator string to the end
print("Hello World")

# The print method may print its parameter without appending
# a line separator string to the end using the end parameter
print("Hello World", end=" ")
print("Hello World")

#The print function may be given strings as well as any of the 
#primitive and object types
print(100)
print(True)
print(100.75)

#We can pass one more more parameters when using the print function
# By default they will be separated by a space.
print(100,True,100.75)

#The default space can be modified and can be made to change To
# Any characters, integer, or string using the sep parameter.
print(100, True, 100.74, sep="-")

#The sep and end parameters mmay be used together in one print statement
print(100, True, 100.75, sep="-", end="!")

#The string % modulo operator can be used with the print function
#for formatting
print("\nHello %s %s. You are %d years old" %("Josh", "Wuller", 20))
print("\nHello %s %s. You are %.2f years old" %("Josh", "Wuller", 20))

#The input function can be used to get data rom standard in
#The returned object will always be a string
first = input('Please enter your first name')
last = input('Please enter your last name')
print(first, last)

age = input('Please enter your age: ')
print('Hello %s %s. You are %s years old.' % (first, last, age))


# print('Hello %s %s. You are %.2f years old.' % (first, last, age))
# This line of code will generate a type error because age is a string, not a float

print(type(first), type(last), type(age))

# we must typecast the returned object if we want to work with it in a form other than Str

intage = int(input('Please enter your age: '))
print('Hello %s %s. You are %d years old.' %(first,last,intage))

floatage=float(input('Please enter your age: '))
print('Hello %s %s. You are %.2f years old' %(first,last,floatage))

# The split function can be used to get multople valus from standard in.
#if a separator isn't given to the function then a white space is used
fname, lname = input('Enter your first and last names separated by a space: ').split()
print(fname, lname)

# a separator, like a comma, may be provided.
fname, lname, tn = input('Enter your first and last names separated by a comma: ').split(',')
print('Hello %s %s. Your phone number is %s.' % (fname,lname,tn))

# We can take in a variable nymber of inputs at a time.
x = [int(x) for x in input('Enter multiple numbers separated by a space: ').split()]
print('Numbers are: ', x)