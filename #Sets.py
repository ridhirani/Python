#Sets
#Operation on sets
print({1,2,3,4,5}.intersection({3,4,5,6}))
print({1,2,3,4,5}.union({3,4,5,6}))
print({1,2,3,4,5}.difference({3,4,5,6}))
print({1,2,3,4,5}.symmetric_difference({3,4,5,6}))
print({1,2,3,4,5}.issuperset({3,4,5,6}))
print({1,2,3,4,5}.issubset({3,4,5,6}))
print({1,2,3,4,5}.isdisjoint({6,7}))
print({1,2,3,4,5}.isdisjoint({3,4,5,6}))

#with single elememyts
print(2 in {3,4,7})
print(2 not in {3,4,7})
s={1,2}
print(len(s))
s.add(3)
print(s)
print(s.discard(7))
print(s.discard(7))
print(s.remove(3))
# print(s.remove(7))
s.update({9,34})
print(s)

#get the unique element of a list
a=["apple","banana","apple","apple","Pear"]
print(list(a))
unique_item=set(a)
print(unique_item)
print(list(unique_item))

#sets of sets
# a={{1,2},{3,4}}
# print(a) # throw error
a1={frozenset({1,2}),frozenset({3,4})}
print(a1)

#Counter is a dictionary where elemets are stored as keys and their
#  counts are stored as values
from collections import Counter
counterA= Counter(['a','b','c','d'])
print(counterA)
