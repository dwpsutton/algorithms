import numpy as np, sys
from datetime import datetime as dt
from numba import jit

fname= "g3.txt"

inf= float("inf")

def readGraph(fname):
    # Add content
    with open(fname,'rb') as f:
        n, m = map(int, f.next().split(' '))
        A= np.zeros([n,n,n]) + inf
        for i in range(n):
            A[i,i,0]= 0
        for line in f:
            i,j,c = map(int, line.split(' '))
            A[i-1,j-1,0]= c
    return A

@jit
def floyd_warshall(A):
    # Assumes initialised A[:,:,0]
    n= A.shape[0]
    for k in range(1,n):
        for i in range(n):
            for j in range(n):
                x1= A[i,j,k-1]
                x2= A[k,j,k-1] + A[i,k,k-1]
                if x1<x2:
                    A[i,j,k]= x1
                else:
                    A[i,j,k]= x2
    return A

def main():
    #Read the graph (ie: initialise A)
    A= readGraph(fname)
    n= A.shape[0]
    minPath= np.min(A)

    #Execute for loop
    tc= dt.now()
    A= floyd_warshall(A)
    print (dt.now() - tc).total_seconds()

    #Check for negative cycle
    for i in range(A.shape[0]):
        if A[i,i,n-1] < 0:
            print 'Negative loop found!'

    #return shortest pair path
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i,j,n-1] < minPath:
                minPath= A[i,j,n-1]
    print 'minimum path= ',minPath

if __name__=="__main__":
    main()
