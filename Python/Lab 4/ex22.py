import matplotlib.pyplot as plt
def twodrand():
    f = open ( 'input2' , 'r')
    l = []
    l = [ line.split() for line in f]
    x=[]
    y=[]    
    n=len(l)       
    for i in range(n-1):
         a=float(l[i][0])
         b=float(l[i][1])
         x.append(a)
         y.append(b)
    plt.plot(x,y,'ro')
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.title("scatter plot for ex2b")


twodrand()
    