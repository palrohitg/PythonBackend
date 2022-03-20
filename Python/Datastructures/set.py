'''
    - Set is an unorderd collections data type that is iterable, mutable and has no dupilcates elements
    - Set, that is has optimized method for checking whether a specific elements is contain in the set. 
    - Based on hashtable known as hashtable.
    - We can't access items using indexes like we do in lists
    - Mutable vs Immutable objects: 
    - https://www.geeksforgeeks.org/sets-in-python/

'''

myset = set([1, 1 , 1])
print(myset)

# adding new elments in the set 
myset.add("d")
myset.update(("vikas",)) # adding the new elements 
myset.remove("d",)
print(myset)

# check if element present / abset 
if 1 in myset:
    print("true")
else:
    print("no")

