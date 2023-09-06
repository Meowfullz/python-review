# Expressions in Python evaluate to true or false.
#Expressions use the comparison operators: <,
# >, <=, >=, ==, !=

x=4

print(x<5)
print(x>5)
print(x==5)
print(x!=5)

# Python supports the if, if-else, if-elif-else, and
# nessted if decision structures.

# The if decision structure tests its condition
#And if the condition is true, it executes the code
# Block its given

if (x<5):
	print('x is less than 5 is true')

# Here is the shorthand version of the if decision
# The shorthand version may be used when there is only
# one sttement to be executed
if (x<5): print('x is less than 5 is true')

# The if-else decision structure tests its condition
# and if the condition is true it executres the code block
# it's given. If the condition is false the code block
#is given to the else is executed

if (x==5):
	print('x is equal to 5 is true')

else:
	print('x is equal to 5 is false.')

#here is the shorthannd version of the if-else decision
print(' x is equal to 5 is true.') if(x==5) else print ('x is equal to 5 is false')

# The if-elif-else decision structure tests multiple
#conditions. Tje code block given to tje condition tuats true,
#is executed. If none of the conditions are true,
#the code the blocks given them to the else is executed

if (x>5):
	print('x is equal to 5 is True')
elif (x==5):
	print('x is equal to 5 is true') 
elif(x<5):
	print('x is less than 5 is true ')

	#This code block wont be executed even 
	#though its condition is true because only
	# the first true code block will be executed
elif (x!=5):
	print('x is not equal to 5 is true')
else:
	print('None of the conditions are true')

# a nested if decision is an if statement that is the target
# of another if statement
if (x<5):
	print('x is less than 5 is true')
	if (x!=5):
		print('x is not equal to 5 is true')

# Comparison operators may be chained together,

a=5
b=10
c=15

if a<b<c:
	print('b is greater than a and less than c. ')


# Python supports the match-case decision structure.
# This decision structure is useful when many conditions need to b tested
# it requires Python 3.10 or newer

grade = 'A'

match grade:
	case 'A':
		print('Super Work!')

	case 'B':
		print('Good job')
	
	case 'C':
		print ('You made it, barely')
	
	case 'D', 'F':
		print('Oh dear....')
	
	case _:
		print('Invalid grade.')


# #Python  supports the ternary operator
# result = 'x is equal to 5 is true' if x (x==5) else 'x is equal to 5 is false'
# print (result)
# print(('x is equal to 5 is true' if x (x==5) else 'x is equal to 5 is false'))

# The ternary operator may be written using tuples
# (false value, true value) [Expression to test]
#x = 5
result = ('x is equal to 5 is false', 'x is equal to 5 is true') [x ==5]
print(result)

# the ternary operator may be written using dictionaries

result = {True :'x is equal to 5 is true', False: 'x is equal to 5 is false.'} [x==5]
print(result)

# Expressions in python may also use the logical operators and, or, and not
num = 150

#This if-else decision structure tests if num is between 1 and 100.
if (num >= 1 and num <= 100):
	print('num is between 1 and 100')
else:
	print('num is not betweej 1 and 100')

#This if-else decision structure tests if num is not between 1 and 100.
if (num < 1 or num > 100):
	print('num is not between 1 and 100')
else:
	print('num is  between 1 and 100')

foundIt = False

#This if-else decision structure tests if foundIt is false.

if (not foundIt):
	print('foundIt is false')
else:
	print('foundIt is True')