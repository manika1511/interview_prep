#The complexity of converting a string to a set is O(n) as time to traverse a string of 'n' characters is O(n) and the time
#to add it to the hash map is O(1) and the is else loop is again O(1)

def all_unique(s):
    l = set(s)
    if len(s) == len(l):
        return "Unique"
    else:
        return "Not unique"

print (all_unique("Reshma"))
print (all_unique("Mamta"))