def second_smallest(numbers):
    m1, m2 = None, None
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
        return m2

def main():
    a = [2,3,1,5,6]
    print (second_smallest(a))

if __name__ == "__main__":
    main()