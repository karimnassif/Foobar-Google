def answer(l):
    count = 0
    doubles = [0] * len(l)

    #This loop checks for lucky doubles in the list and
    #adds them to the doubles list.
    for x in xrange(len(l)-1):
        for y in xrange(x):
            if l[x]%l[y]==0:
                doubles[x]+=1
    
    #This loop functions exactly the same as the previous,
    #except for any double found where x%y==0, it checks
    #the doubles array to see if (and how many) doubles exist
    #with y as the first number, as this would mean a lucky triple.
    for x in xrange(len(l)):
        for y in xrange(x):
            if l[x]%l[y] == 0:
                count += doubles[y]
    return count
