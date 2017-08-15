"""Implement a method to perform basic string compression using the counts of repeated characters. Traversing a string 
wil take O(n) time and all other operations are O(1). So, the entire algorithm has O(n) time complexity. """

def string_compressor(s):
    output = ""
    counter = 1

    for i in range(len(s)):
        if output == "":                #adding the first element in the output
            output = output + s[i]
        elif output[-1] != s[i]:        #checking if the last element in output is same as input string current element
            output = output + str(counter) + s[i] #appending the count to the string and the next element
            counter = 1
        else:
            counter = counter + 1       #increasing the counter if same

    output = output + str(counter)
    return output

def main():
    string = input("Enter a string: ")
    print (string_compressor(string))

if __name__ == '__main__':
    main()

