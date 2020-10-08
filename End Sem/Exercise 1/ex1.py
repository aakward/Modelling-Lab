import random
def main():
    x=0     #the initial position of vehichle-1 is the origin
    y=0     #the initial position of vehichle-2 is the origin
    t=0     #time 
    while((abs(x)+abs(y))>0.01 or t==0):     
        r1=random.uniform(-2,2)
        r2=random.uniform(-2,2)
        x=x+r1             #position of vehichle-1 after t mins
        y=y+r2             #position of vehichle-2 after t mins
        print x,y
        t=t+2
    print "The two vehichles are expected to meet again after ",t,"minutes."

main()