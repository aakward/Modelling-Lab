import matplotlib.pyplot as plt
def testrand2():
    v=open('input1')
    g=list(v)
    a=[]
    for i in g:
        a.append(float(i))
    k=input("Enter the no. 'k': ")
    n=len(a)
    b=[]    
    for i in range(0,n,k):
        b.append(a[i])
    plt.hist(b)
    plt.xlabel("values")
    plt.ylabel("frequency")
    plt.title("histogram for 1d")

testrand2()
        