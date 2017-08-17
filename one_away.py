"""Given two strings, write a function to check if they are one edit (or zero edits) away.
Covert the strings into sets and then check the conditions using set operations.
Making set: O(n); taking difference: O(n+n) approx
"""

def one_away(s1,s2):
    set1 = set(s1)
    set2 = set(s2)

    if len(set1) != len(set2):      #if different length
        if (len(set1-set2) == 1 or len(set2-set1) == 1):    #the set difference can have just one element(add or remove)
            return True
        else:
            return False
    else:
        if len(set1-set2) == 1 and len(set2-set1) == 1:     #if same length then one letter is different, so both side difference
                                                    #has one element
            return True
        else:
            return False

def main():
    s1 = input("Enter first string: ")
    s2 = input('Enter second string: ')
    print (one_away(s1, s2))

if __name__ == '__main__':
    main()

