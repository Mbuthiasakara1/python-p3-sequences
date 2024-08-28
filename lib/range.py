#can only contain intergers in a fixed pattern
#it only requires one argument

# This code iterate thru the numbers 0 to 3 and print each number
for n in range(4):
    print(n)

# This code will iterate through the numbers 1 to 3 (up to but not including 4) and print each number.
for n in range(1,4):
    print(n)

# This code will iterate through the numbers starting at 0, up to but not including 4, with a step size of 2. It will print each number.
#  2 is the step size yani go up by 2
for n in range(0,4,2):
    print(n)


 #DIFFERENCE BTN LIST AND RANGE
    # in LIst
my_list = [0, 1, 2, 3]
print(my_list) 
# => [0, 1, 2, 3]

# when you print a range object directly it shows its rep which includes the start,stop,step values.THis is beacause a 'range object is not a list of numbers but rather an iterable that generates numbers on demand
# my_range=range(4)
# creates range obj that rep a sequnce of numbers from 0 to 3 which step default 1
my_range= range(2,10,2)
print(my_range)

# strings

my_string = 'Hello World!'
for char in my_string:
    print(char)
    print(my_string[0])

 #string methods
# str.upper() returns an uppercase version of the original string.
# str.lower() returns a lowercase version of the original string.
# str.title() returns the original string in titlecase (with the first letter of each new word capitalized.) 