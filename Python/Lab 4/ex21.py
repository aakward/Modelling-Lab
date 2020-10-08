import matplotlib.pyplot as plt
import random
def twodrand():
    n=input("Enter the no. 'n': ")
    x=[]
    y=[]
    for i in range(n):
        r1=random.random()
        r2=random.random()
        x.append(r1)
        y.append(r2)
    plt.plot(x,y,'ro')
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.title("Scatter plot to check randomness")
    
twodrand()