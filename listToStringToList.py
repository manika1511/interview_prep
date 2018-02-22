l = ["abc", "de", "fghi", "j"]

ptr=[]
ptr.append(0)

def listToStr(strList):
    result=''
    for item in strList:
        result=result + item
        ptr.append(len(result))
    return result

def strToList(str):
    result=[]
    i=0
    while i < len(ptr) and i+1 < len(ptr):
        result.append(str[ptr[i]: ptr[i+1]])
        i = i + 1
    return result


s = listToStr(l)
print (s)

lr=strToList(s)
print (lr)

