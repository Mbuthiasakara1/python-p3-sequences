my_list=[1,2,3,4]
print(my_list[2])

fibonacci_list =[0,1,2,3,5,8,13,21]

s=[2,3,4,5,6]
print(11 in s)
# example 2

s = [1,2,3]
s2=[4,5,6]
result= s+s2
print(result)

s=[1,2,4]
result=s*2
print(result)
#s[i:j] returns a slice of s from index i up to (but not including!) index j.
s="Hello, world!"
print(s[0:5])

#s[i:j:k] returns a slice of s from i to j with steps of k in between.
s="Hello, world!"
print(s[0:12:2])
#inachukua the second element up 
#prints the length
s=[0,2,4,5,1,7,3,1,3,1]
print(len(s))
print(min(s))#prints the minimum no in the list
print(max(s))#prints the maximum no in the list
print(s.index(1))#prints the index of the character in the fisrt occurence
print(s.count(1))#prints the no of times the element has occurred in the list
print(s[len(s) -2])