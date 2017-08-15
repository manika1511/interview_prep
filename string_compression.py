def string_compressor(s):
    output = ""
    counter = 1

    for i in range(len(s)):
        if output == "":
            output = output + s[i]
        elif output[-1] != s[i]:
            output = output + str(counter) + s[i]
            counter = 1
        else:
            counter = counter + 1

    output = output + str(counter)
    return output

def main():
    string = input("Enter a string: ")
    print (string_compressor(string))

if __name__ == '__main__':
    main()

