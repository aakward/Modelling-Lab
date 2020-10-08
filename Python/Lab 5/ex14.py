import random
import matplotlib.pyplot as plt
def qty_sd():
    m=input("Enter the mean of the demand: ")
    cp=input("Enter cost price of milk: ")
    sp=input("Enter selling price of milk: ")
    slp=input("Enter salvage price of milk: ")
    sd=[5.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0]    
    d=[]
    avg_profit=0.0
    maxx=0.0
    profit=[]
    tot_profit=0.0
    opt_qty=[]
    n=input("Enter the no. of days for which milk is to be sold: ")
    for i in range(n):
        d.append(0)
        profit.append(0)
    for i in range(len(sd)):
        opt_qty.append(0)
    for x in range(len(sd)):
        l=m-2*sd[x]
        u=m+2*sd[x]    
        maxx=0.0        
        for stock in range(int(l),int(u+1)):
            avg_profit=0.0       
            for iteration in range(10):
                tot_profit=0.0            
                for k in range(n):
                    r=random.gauss(m,sd[x])
                    d[k]=r
                    if(d[k]>=stock):
                        profit[k]=(sp*stock)-(cp*stock)
                    if(d[k]<stock):
                        profit[k]=(sp*d[k])+((stock-d[k])*slp)-(cp*stock)
                    tot_profit=tot_profit+profit[k]
                avg_profit=avg_profit+((tot_profit)/n)
            if(avg_profit>maxx):
                maxx=avg_profit
                opt_qty[x]=stock
    plt.plot(sd,opt_qty,"ro")
    plt.xlabel("sd")
    plt.ylabel("Optimal Quantity")
    plt.title("Scatter plot of Optimal Qty. against SD")

qty_sd()