def topten():
    n=1
    while n<=5:
        sq=n*n
        yield sq
        n=n+1


for i in topten():
    print(i)