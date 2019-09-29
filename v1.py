def getinp(mylist, parts):
    return [myList[(i*len(myList))//parts:((i+1)*len(myList))//parts] for i in range(parts)]

getinp(range(10), 3)
