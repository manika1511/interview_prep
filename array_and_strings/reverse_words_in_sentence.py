def reverse_string(str, start, end):
    if len(str) == 0:
        return None
    s = list(str)
    while start < end:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp

        start = start + 1
        end = end - 1

    return "".join(s)

def reverse_words(str):
    reverse_str = reverse_string(str, 0, len(str)-1)
    print (reverse_str)
    i = 0
    while i < len(reverse_str):
        j = i
        while i < len(str) and reverse_str[i] != " ":
            i = i + 1

        print (j, i-1)
        if i-1 < len(str):
            reverse_str = reverse_string(reverse_str,j,i-1)
            i = i + 1
    return reverse_str

def main():
    str = "What is your name"
    print (reverse_words(str))

if __name__ == "__main__":
    main()