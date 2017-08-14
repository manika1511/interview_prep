"""URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient 
space at the end to hold the additional characters, and that you are given the "true" length of the string"""

def urlify(s,l):
    # result = s.replace(" ","%20")
    result = "%20".join(s.split(" "))
    return result[0:l]


def main():
    user_input = input("Enter a string: ")
    length = int (input("Enter length of the string: "))
    print (urlify(user_input, length))

if __name__ == '__main__':
    main()