def all_unique(s):
    l = set(s)
    if len(s) == len(l):
        return "Unique"
    else:
        return "Not unique"

print (all_unique("Reshma"))
print (all_unique("Mamta"))