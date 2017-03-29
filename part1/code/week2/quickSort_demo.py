#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np
import sys, copy


def swap(x,i,j):
    buff= copy.deepcopy(x[j])
    x[j]= x[i]
    x[i]= buff
    return x

def choosePivots(x, method= 'random'):
    middleElement= lambda x: int(np.floor(len(x)/2.-0.5))
    if method == 'median-of-three':
        if len(x) >= 3:
            medianCandidates= [0,middleElement(x), len(x)-1]
            vals= map(lambda i: x[i], medianCandidates)
            m= np.median(vals)
            return medianCandidates[ np.argmin( map(lambda i: abs(x[i]-m),medianCandidates) ) ]
        else:
            return 0
    else:
        return choosePivot(len(x),method=method)

def choosePivot(n,method='random'):
    allowed= {'random','first','last'}
    if method in allowed:
        if method == 'random':
            return np.random.random_integers(0,high=n-1,size=1)[0]
        elif method == 'first':
            return 0
        elif method == 'last':
            return n-1
    else:
        print 'Unknown method supplied: ',method
        sys.exit(-1)



def partition(x,l):
    n= len(x)
    pivot= copy.deepcopy( x[l] )
    if l != 0:
        swap( x, 0, l) # Initialise with pivot at start
    i = 1
    for j in range(1,n):
        if x[j] <= pivot:
            x= swap(x,i,j)
            i+=1
    swap( x, 0, i-1) # Now put pivot in its rightful place
    return x, i-1


def quickSort(x, method= 'random'):
    n= len(x)
    if n == 0 or n == 1:
        # base cases
        return x, 0
    else:
        l= choosePivots(x,method=method)
        ctr= n-1
        x, i = partition(x,l)
        #        print l,x[:i],x[i],x[i+1:]   #Useful print for debugging
        x1, ctr1= quickSort( x[:i], method=method )
        x2, ctr2= quickSort( x[i+1:], method=method )
        return  x1 + [x[i]]+ x2, ctr+ctr1+ctr2  # This is a list concatenate



# This tests whether an array is ordered
def tester(x):
    n= len(x)
    ok= True
    for i in range(n-1):
        if x[i] > x[i+1]:
            print 'Problem',i,i+1
            ok= False
    return ok


if __name__ == '__main__':
    testArray= [83,65,820,1,78,83,46,5,920,65]
    #print testArray
    #print swap(testArray,2,5)
    #for l in range(len(testArray)):
    #    testArray= [83,65,820,1,78,46,5,920]
    #    print l, testArray[l]
    #    print partition(testArray,l)
    sorted, ctr= quickSort(testArray,method='random')
    print ctr
    print ''
    print sorted
    print tester(sorted)

    testArray= range(10)
    sorted, ctr= quickSort(testArray,method='first')
    print ctr # worst case O(n) example
    print ''
    print tester(sorted)

    testArray= range(10000)
    np.random.shuffle(testArray)
    sorted, ctr= quickSort(testArray,method='random')
    print ctr
    print ''
    print tester(sorted)