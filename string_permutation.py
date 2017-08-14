"""Checking if a string is a permutation of the other with O(n) time complexity. In this, the two strings are converted
into dicts and then those dicts are compared"""

from collections import Counter

def check_permutation(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):      #if length is not equal, then definitely not a permutation
        return False
    dict1 = Counter(s1)         #converting into dict containing letter and its frequency
    dict2 = Counter(s2)
    if dict1 == dict2:          #comparing two dicts
        return True
    else:
        return False

def main():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print (check_permutation(s1,s2))

if __name__ == '__main__':
    main()


