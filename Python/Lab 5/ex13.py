import random
def max_prof():
    m=input("Enter the mean of the demand: ")
    sd=input("Enter the sd of the demand: ")
    cp=input("Enter cost price of milk: ")
    sp=input("Enter selling price of milk: ")
    slp=input("Enter salvage price of milk: ")
    d=[]
    avg_profit=0.0
    maxx=0.0
    profit=[]
    tot_profit=0.0
    opt_qty=0
    n=input("Enter the no. of days for which milk is to be sold: ")
    for i in range(n):
        d.append(0)
        profit.append(0)
    l=m-2*sd
    u=m+2*sd    
    for stock in range(l,u+1):
        avg_profit=0.0       
        for iteration in range(10):
            tot_profit=0.0            
            for k in range(n):
                r=random.gauss(m,sd)
                d[k]=r
                if(d[k]>=stock):
                    profit[k]=(sp*stock)-(cp*stock)
                if(d[k]<stock):
                    profit[k]=(sp*d[k])+((stock-d[k])*slp)-(cp*stock)
                tot_profit=tot_profit+profit[k]
            avg_profit=avg_profit+((tot_profit)/n)
        if(avg_profit>maxx):
            maxx=avg_profit
            opt_qty=stock
    print "Optimum Quantity of milk is: ",opt_qty
    
    
max_prof()
    
        
            
                    
                
        
            