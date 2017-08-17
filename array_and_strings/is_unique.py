"""The complexity of converting a string to a set is O(n) as time to traverse a string of 'n' characters is O(n) and the time
to add it to the hash map is O(1) and the is else loop is again O(1).
Assumption: the lowercase and uppercase letters are considered same"""

def all_unique(s):
    s = s.lower()           #converting string to lower case
    l = set(s)              #converting string to set
    if len(s) == len(l):    #checking the length of the string and set
        return "Unique"
    else:
        return "Not Unique"

"""Solving using no other data structure. In this bitwise operators are used to check a bit if it is present and 
if the checked bit is accessed again then the string doesn't have unique letters"""

def all_unique_nods(s):
    s = s.lower()
    checker = 0 #taking 0 as a checker

    for ch in s:
        val = ord (ch) - ord ('a') #subtracting the ascii values
        if (checker & (1 << val)) > 0: #checking if the bit is already 1
             return "Not Unique"

        checker = checker|(1 << val)   #if not already 1, then set to 1
    return "Unique"

def main():
    s = input("Enter a string: ")
    print("Result using set: " + all_unique(s))
    print("Result using no other data structure: " + all_unique_nods(s))

if __name__ == "__main__":
    main()

