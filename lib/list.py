#list.sort()
my_list=[3,6,4,2,1,5]
my_list.sort()
print(my_list)

#sorting strings
my_list=['carrots','apples','oranges','banana','oranges']
my_list.sort()
print(my_list)

# we can apss parameters to sort to allow the function to be more versatile
#The key parameter allows us to pass in a function which can server as a key for the sort comparison
#The key=len argument tells the sort() method to use the length of each element as the basis for sorting. In other words, elements will be sorted by their lengths.
#elements with shoter lenghts come before

my_list =['This is a long sentence', 'Word', 'z']

my_list.sort(key = len)
print(my_list)

#Sort in descending order
#reverser.length modifies the sorting to be in descending order, meaning that elements with longer lengths come before elements with shorter lengths.
my_list =['This is a long sentence', 'Word', 'z']
my_list.sort(key = len, reverse=True)
print(my_list)

#sorting complex data structures
#my_list every element is a tuple,contains name and number
#sort_tuple  takes input and returns joe atuple_value[0] which will be used as the sorting key
my_list = [('john',2),('Steve',1),('Joe',0)]

def sort_tuple(tuple_value):
    return tuple_value[0]
my_list.sort(key =sort_tuple) 
print(my_list)   

#Sorted() returns a sorted copy of the original list
#should be used when you want to preserver the intergrity of your original list.
#same as sort
my_list =[3,6,4,2,1,5]
sorted_list =sorted(my_list)
print(sorted_list)

my_list = ['Loquacious', 'Chatty', 'Talkative']
sorted_list=sorted(my_list,key=len,reverse=True)
print(sorted_list)

#Adding to List
#we can modify a list using the ,elements index
my_list=[1,2,3,4]
my_list[0]=None
print(my_list)

#WE can extend lists using
#list.append(),list.insert()
my_list=[0,1,2,3,4]
my_list.append(4)#adds at the end of the list at the emd
print(my_list)

#list.insert()
#can insert at an index
# takes two arguments,index and a value
# if a value already exists at the index,the new value is inserted before it and everything after is moved up by 1,if no value exists at the index ,the new value is added at the end of the existing list
my_list=["a","b","c","d","f"]
my_list.insert(4,"z")
my_list.insert(6,"y")
print(my_list)
