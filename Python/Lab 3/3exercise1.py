import matplotlib.pyplot as plt
import pylab as p1
def main():
    v=open('demand.txt')
    g=list(v)
    d=[]
    for i in g:
        d.append(int(i))
    n=len(d)
    x=0.0
    x2=0.0
    for i in range(n):
        x=x+d[i]
        x2=x2+(d[i]**2)
    x=x/n
    x2=(x2/n)-(x**2)
    x2=x2**(0.5)
    print "The mean is: ", x
    print "The standard deviation is: ",x2
    plt.plot(d)
    plt.xlabel("time")
    plt.ylabel("demands")
    plt.title("Line diagram for Demands over time")
    plt.savefig("demand over time.pdf")
    plt.clf()
    plt.hist(d)
    plt.xlabel("demands")
    plt.ylabel("frequency")
    plt.title("Histogram for demands")
    plt.savefig("Histogram for demands.pdf")
    plt.clf()    
    exp_demand=x
    if(exp_demand>1000):
        stock_left=0
    else:
        stock_left=1000-exp_demand
    exp_profit=(min(exp_demand,1000)*6)+(stock_left*(-2))
    print '''the avg. profit Akbar would have made if he packs 1000L and expects
            demand to be the mean of the past 500days is: ''', exp_profit
    stock=[]
    profit=[]
    for i in range(10):
        p=input("Enter a stock quantity: ")
        if(exp_demand>p):
            stock_left=0
        else:
            stock_left=p-exp_demand
        exp_profit=(min(exp_demand,p)*6)+(stock_left*(-2))
        stock.append(p)
        profit.append(exp_profit)
    p1.plot(stock,profit,'or')    
    p1.axis([0,1600,0,8000])    
    p1.xlabel("Stock")
    p1.ylabel("Profit")
    p1.title("Scatter diagram for Profit against Stock")
    p1.show()
    p1.savefig("Profit against Stock")
    
main()