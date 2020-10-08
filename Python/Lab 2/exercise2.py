import matplotlib.pyplot as plt
def ex2fun():
    v=open("ex2a.txt")
    g=list(v)
    a=[]
    for i in g:
        a.append(int(i))
    m=input("Enter an integer: ")
    n=len(a)
    n=n-(n%m)
    b=[]
    for i in range(0,n,m):
        sum=0.0
        for j in range(i,i+m):
            sum=sum+a[j]
        sum=sum/m
        b.append(sum)
    print(b)
    l=len(b)
    print "The no. of elements in b[] is: ", l
    min=b[0]
    max=b[0]
    for i in range(l):
        if (b[i]<min):
            min=b[i]
        if (b[i]>max):
            max=b[i]
    print "the minimum value in the array is: ", min
    print "the maximum value in the array is: ", max
    sum=0.0
    for i in range(l):
        sum=sum+b[i]
    sum=sum/l
    print "The average value of elements of b is: ", sum
    x=0.0
    for i in range(l):
        x=x+(b[i]**2)
    x=x/l
    var=0.0
    var=x-(sum**2)
    var=var**(.5)
    print "SD of the array b[] is: ", var
    plt.hist(b)
    plt.title("Histogram for ex2a")
    plt.xlabel("values")
    plt.ylabel("Frequency")
    plt.show()
    
ex2fun()   
    
    
