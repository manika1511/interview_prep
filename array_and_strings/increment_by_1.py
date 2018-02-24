#increment a number by 1

def increment(arr):
    carry = 1 #as one needs to be added
    sum = 0
    i = len(arr) - 1
    while i >= 0:
        sum = arr[i] + carry
        carry = int(sum/10)
        arr[i] = int(sum%10)
        i = i - 1
    return arr

def main():
    arr = [0,8,9,9,9]
    print (increment(arr))

if __name__ == "__main__":
    main()

