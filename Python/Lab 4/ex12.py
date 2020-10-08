import matplotlib.pyplot as plt
def testrand():
    v=open('input1')
    g=list(v)
    a=[]
    for i in g:
        a.append(float(i))
    plt.hist(a)
    plt.xlabel("values")
    plt.ylabel("frequency")
    plt.title("Histogram for qsn 1b")
    
testrand()    
    
    