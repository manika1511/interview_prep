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

def check_permutation2(s1, s2): #considering case-sensitivity
    d1 = dict()
    if len(s1) != len(s2):
        return False

    for char in s1:
        if char in d1:
            d1[char] = d1[char] + 1
        else:
            d1[char] = 1
    for char in s2:
        if char not in d1:
            return False
        else:
            d1[char] = d1[char] - 1
            if d1[char] < 0:
                return False

    if sum(d1.values()) != 0:
        return False
    else:
        return True

def check_permutation3(s1, s2): #considering case-sensitivity and using constant space
    check = [0]*128
    if len(s1) != len(s2):
        return False

    for char in s1:
        check[ord(char)] = check[ord(char)] + 1
    for char in s2:
        check[ord(char)] = check[ord(char)] - 1
        if check[ord(char)] < 0:
            return False

    if sum(check) != 0:
        return False
    else:
        return True

def main():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print (check_permutation3(s1,s2))

if __name__ == '__main__':
    main()


