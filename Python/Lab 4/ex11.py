import random
import matplotlib.pyplot as plt
def testrand():
    n=input("Enter the no 'n': ")
    a=[]    
    for i in range(n):
        r=random.random()
        a.append(r)
    plt.hist(a)
    plt.xlabel("values")
    plt.ylabel("frequency")
    plt.title("Histogram for qsn 1a")

testrand()
        
