"""
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to 
isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").
"""

def string_rotation(s1, s2):
    if len(s1) != len(s2):  #check if lengths are same
        return False
    if s2 in s1*2:          #if rotation, then must be substring of twice the string
        return True
    else:
        return False

def main():
    assert string_rotation("hello", "lohel") == True
    assert string_rotation("waterbottle", "erbottlewat") == True
    assert string_rotation("hello", "olhel") == False

if __name__ == "__main__":
    main()