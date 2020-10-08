import matplotlib.pyplot as plt
def main():
    v=open("tv.txt")
    g=list(v)
    d=[]
    for i in g:
        d.append(int(i))
    n=len(d)
    store=[]                    #array for storing inventory in store
    wh=[]                       #array for storing inventory in warehouse
    dc=[]                       #array for storing inventory in distribution center
    ac=[]                       #array for storing inventory in assembly center
    tc=0.0                      #total inventory cost
    waitl=0.0                   #no. of customers waitlisted
    wc=0.0
    dem=[]                      #total back-ordering cost
    for i in range(1):          #start of part-a
        store.append(5000)
        wh.append(5000)
        dc.append(5000)
        ac.append(5000)
        dem.append(d[i])
    for i in range(1,n):
        store.append(0)
        wh.append(0)
        dc.append(0)
        ac.append(5000)
        dem.append(d[i])
    for i in range(n):
        if(i!=n-1):
            if(waitl>0):
                d[i+1]=d[i+1]+waitl
                wc=wc+(waitl*110)
                waitl=0
            if(store[i]-d[i]>=0):            
                store[i+1]=store[i]-d[i]+wh[i]
            else:
                waitl=d[i]-store[i]
                store[i+1]=wh[i]
            wh[i+1]=dc[i]
            if(i==0):
                dc[i+1]=0
            else:
                dc[i+1]=ac[i-1]
            tc=tc+(store[i]*100)+(wh[i]*80)+(dc[i]*60)+(ac[i]*50) 
        else:
            waitl=max(0,d[i]-store[i])
            wc=wc+(waitl*110)            
            tc=tc+(store[i]*100)+(wh[i]*80)+(dc[i]*60)+(ac[i]*50)
    print "The total cost of inventory for these 100 weeks is: ", tc
    print "The total cost of backordering for these 100 weeks is: ", wc
    print "Total cost is :",tc+wc
    plt.plot(store) 
    plt.plot(wh)
    plt.plot(dc)  
    plt.plot(ac)
    plt.legend('swda')
    plt.ylabel("Inventory level")    
    plt.savefig("multiple line diag1")
    plt.clf()
    bestamt=tc+wc                       #start of part b
    bestqty=5000.0
    l=input("Enter the lower limit of the quantity: ")
    u=input("Enter the upper limit of your quantity: ")    
    for j in range(l,u+1):
        store[0]=j
        wh[0]=j
        dc[0]=j
        ac[0]=j
        d[0]=dem[0]        
        for k in range(1,n):
            store[k]=0
            wh[k]=0          
            dc[k]=0
            ac[k]=j
            d[k]=dem[k]
        tc=0.0
        waitl=0.0        
        wc=0.0
        for i in range(n):
            if(i!=n-1):
                if(waitl>0):
                    d[i+1]=d[i+1]+waitl
                    wc=wc+(waitl*110)
                    waitl=0
                if(store[i]-d[i]>=0.0):            
                    store[i+1]=store[i]-d[i]+wh[i]
                else:
                    waitl=d[i]-store[i]
                    store[i+1]=wh[i]
                wh[i+1]=dc[i]
                if(i==0):
                    dc[i+1]=0.0   
                else:
                    dc[i+1]=ac[i-1]
                tc=tc+(store[i]*100)+(wh[i]*80)+(dc[i]*60)+(ac[i]*50) 
            else:
                waitl=max(0,d[i]-store[i])
                wc=wc+(waitl*110)            
                tc=tc+(store[i]*100)+(wh[i]*80)+(dc[i]*60)+(ac[i]*50)
        
        if((tc+wc)<bestamt):
            bestqty=j
            bestamt=tc+wc
    print "The best quantity among the ones entered is: ", bestqty
    print "The lowest total cost is: ", bestamt
    
   
    
    
    
   
    
main()
            
                
                
            
                
            
            
                
                      
        
        