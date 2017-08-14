"""The complexity of converting a string to a set is O(n) as time to traverse a string of 'n' characters is O(n) and the time
to add it to the hash map is O(1) and the is else loop is again O(1).
Assumption: the lowercase and uppercase letters are considered same"""

def all_unique(s):
    s = s.lower()
    l = set(s)
    if len(s) == len(l):
        return "Unique"
    else:
        return "Not Unique"

"""Solving using no other data structure. In this bitwise operators are used to check a bit if it is present and 
if the checked bit is accessed again then the string doesn't have unique letters"""

def all_unique_nods(s):
    s = s.lower()
    checker = 0

    for ch in s:
        val = ord (ch) - ord ('a')
        if (checker & (1 << val)) > 0:
             return "Not Unique"

        checker = checker|(1 << val)
    return "Unique"

assert all_unique_nods("Jonathan") == "Not Unique", "not unique"
assert all_unique_nods("Rose") == "Unique", "is unique"
assert all_unique("Jonathan") == "Not Unique", "not unique"
assert all_unique("Rose") == "Unique", "is unique"



