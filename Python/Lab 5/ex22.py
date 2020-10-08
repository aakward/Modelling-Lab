import random
def simvirus():
    n=input("Enter total no. of students in the class: ")
    a=[]
    a.append(0)
    for i in range(1,n):
        a.append(1)
    k=0
    i=0       
    print "The computers infected by the virus are: " 
    print "1th computer" #we assume the first computer is bindu's computer
    while(2>1):
        r=random.randint(0,n-1)
        if (r==i):         #a virus cannot spread from a computer again to that particular computer 
            while(r==i):
                r=random.randint(0,n-1)
        print (r+1),"th computer"
        k=k+1
        if(a[r]==0):
            break
        else:
            a[r]=0
        i=r
    print "The no. of computers infected is: ",k

simvirus()
            
        
        