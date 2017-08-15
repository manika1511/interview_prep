"""Given a string, write a function to check if it is a permutation of a palin-drome.
Check the count of each character. If it is a permutation of a palindrome, only one character can have odd count..
All others will have even count.. 
Making a dict is O(n) and for going through dict maximum O(n).. So total O(n+n).. O(n)"""

from collections import Counter

def palin_permutation(s):
    s = s.lower()
    d = Counter(s)      #make dict of the characters
    del d[' ']          #del the key ' '
    odd_occurred = False

    for value in d.values():
        if value %2 != 0:               #check if count is odd
            if odd_occurred == True:    #if already True, it cannot be a permutation of palindrome
                return False
            else:
                odd_occurred = True #set odd_occurred to True if the first occurrence
    return True

def main():
    s = input("Enter a string: ")
    print (palin_permutation(s))

if __name__ == '__main__':
    main()