#given two strings, tell whether they are anagrams or not
def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    char = [0]*128
    for i in str1:
        char[ord(i)] = char[ord(i)] + 1
    for i in str2:
        char[ord(i)] = char[ord(i)] - 1
        if char[ord(i)] < 0:
            return False
    if char != [0]*128:
        return False
    return True

def main():
    str1 = "Manika"
    str2 = "manika"
    print (isAnagram(str1,str2))

if __name__ == "__main__":
    main()