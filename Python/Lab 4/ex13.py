import random
import matplotlib.pyplot as plt
def testrand2():
    n=input("Enter the no. 'n': ")
    k=input("Enter the no. 'k': ")
    a=[]   
    b=[]
    for i in range(0,n):
        r=random.random()
        a.append(r)
    for i in range(0,n,k):
        b.append(a[i])
    plt.hist(b)
    plt.xlabel("values")
    plt.ylabel("frequency")
    plt.title("histogram for 1c")
    
testrand2()