import matplotlib.pyplot as plt
def ex1fun():
    v=open("ex1a.txt")
    g=list(v)
    a=[]
    for i in g:
        a.append(int(i))
    print(a)
    n=len(a)
    print "the no. of elements in the array is: ", n
    min=a[0]
    max=a[0]
    for i in range(n):
        if (a[i]<min):
            min=a[i]
        if (a[i]>max):
            max=a[i]
    print "the minimum value in the array is: ", min
    print "the maximum value in the array is: ", max
    for i in range(min+1,max):
        count=0
        for j in range(0,n):
            if(a[j]==i):
                count=count+1
        if(count>0):
            print "The no of times", i ,"occurs is: ", count
    x=0.0
    x2=0.0
    sd=0.0
    var=0.0
    for i in range(0,n):
        x=x+a[i]
        x2=x2+(a[i]**2)
    x=x/n
    x2=x2/n
    var=x2-(x**2)
    sd=var**(.5)
    print "the average value of the elements of the vector is: ", x
    print "the sd of the elements of a is: ",sd
    plt.hist(a)
    plt.title("Histogram for ex1a")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
ex1fun()    
    
    
                
    
                
        
     
        
        
