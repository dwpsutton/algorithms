#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np,copy,sys

checker= {}

def readData(fname):
    f= open(fname,'rb')
    l= f.readline().strip(' ')
    sackSize= int(l.split()[0])
    numItems= int(l.split()[1])
    w= np.zeros(numItems)
    v= np.zeros(numItems)
    for i in range(numItems):
        line= f.readline().split()
        v[i]= int(line[0])
        w[i]= int(line[1])
    return v,w,sackSize



if __name__ == "__main__":
    sys.setrecursionlimit(2005)
    fname= 'knapsack1.txt'
    v,w,l= readData(fname)

    def rCheck(i,x):
        if i in checker:
            if x in checker[i]:
                return checker[i][x]
        else:
            checker[i]= {}
        if i < 0:
            return 0.0
        else:
            t2= rCheck(i-1,x)
            if x-w[i] >= 0:
                tt1= rCheck(i-1,x-w[i])
                t1= tt1+v[i]
            else:
                t1= 0.0
        result= max([t1,t2])
        checker[i][x]= result
#        print i,x,checker[i][x],'end1'
        return checker[i][x]

    print rCheck(len(v)-1,l)
#    print checker
