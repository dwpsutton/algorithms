#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np,copy


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
    fname= 'knapsack1.txt'
    v,w,l= readData(fname)
    grid= np.zeros( (len(v), l+1) )
    for i in range(len(v) ):
        for j in range( l+1 ):
            if j-w[i] >= 0:
                if i==0:
                    exclude= 0
                    include= v[i]
                else:
                    exclude= grid[i-1,j]
                    include= grid[i-1,j-w[i]] + v[i]
                grid[i,j]= max( [exclude, include] )
    print grid[-1,-1]
