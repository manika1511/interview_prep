import math

def printSine(rows):
    maxWidth = 40
    for x in range(rows):
        angle = (x*3.14)/(rows)
        # print(angle)
        width = math.floor(maxWidth * math.sin(angle))
        # print (width)
        for j in range(width):
            print("*",  end="")
        print('\n')

printSine(20)
