#Removing from the list
#THE METHODS
# The del() function.
# The list.pop() method.
# The list.remove() method.
# The list.clear() method.

# 1)del
# removes elements from a list,specificed by an index or range of indices.

my_list=['a', 'b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0])
print(my_list)

del(my_list[0:1])
print(my_list)

# 2)pop removes and returns the element at the index passed in as an argument.
# when used without any arguments it removes and returns the last element of the list
my_list=['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list.pop()#removes the last element of the list
my_list.pop(0)
print(my_list)

#3)List.remove()
#removes the element passed in as argument.This is one of the few list methods that serached by vakue instead of list

my_list=['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list.remove('f')
my_list.clear()
print(my_list)
