import random
import matplotlib.pyplot as plt
def simvirus():
    n=input("Enter total no. of students in the class: ")
    run=input("Enter the no. of runs: ")
    a=[]
    count=[]
    a.append(0)
    for i in range(1,n):
        a.append(1)
    for j in range(run):
        a[0]=0
        for i in range(n):
            a[i]=1
        k=0
        i=0       
        while(5>0):
           r=random.randint(0,n-1)
           if (r==i):         #a virus cannot spread from a computer again to that particular computer 
               while(r==i):
                   r=random.randint(0,n-1)
           
           k=k+1
           if(a[r]==0):
               break
           else:
               a[r]=0
           i=r
        count.append(k)
    print(count)
    mean=0.0
    var=0.0
    for i in count:
        mean=mean+i
        var=var+(i**2)
    mean=mean/run
    var=(var/run)-(mean**2)
    print "Mean no. of computers affected is: ",mean
    print "Variance of the no. of computers affected is: ",var
    plt.hist(count)
    plt.xlabel("values of k")
    plt.ylabel("frequency")
    plt.title("Histogram for No. of computers affected")
    
simvirus()