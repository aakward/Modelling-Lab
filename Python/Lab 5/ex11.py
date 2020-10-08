import random
import matplotlib.pyplot as plt
def randfn():
    d=[]
    l=0
    m=0
    n=input("Enter the no. of data points you want to draw from gaussian distn: ")
    for i in range(n):
        r=random.gauss(500,30)
        d.append(r)
        if(r>590):
            m=m+1
        if(r<410):
            l=l+1
    print "The no. of times demand is more than 590L is: ", m
    print "The no. of times demand is less than 410L is: ", l
    p=[]
    for i in range(n):
        if(d[i]>500):
            p.append(500*6)
        if(d[i]<500):
            p.append((d[i]*6)+((500-d[i])*(-2)))
        print "Profit for ",(i+1),"th day is: ",p[i]
    plt.hist(p)
    plt.xlabel("Profit")
    plt.ylabel("Days")
    plt.title("Histogram for the distribution of profit")
    mean=0.0
    var=0.0
    for i in range(n):
        mean=mean+p[i]
        var=var+(p[i]**2)
    mean=mean/n
    var=(var/n)-(mean**2)
    print "The mean profit is:",mean
    print "The variance of the profit is: ",var
    
    

randfn()
    
    
    
    
    