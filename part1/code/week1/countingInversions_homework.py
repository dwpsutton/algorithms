#!/Users/davidsutton/usr/canopy/bin/python

# This homework counts inversions in a 1D integer array without repeated values.

def mergeCount(a,b):
    na= len(a)
    nb= len(b)
    c= []
    ctr= 0
    while nb + na > 0:
        if nb == 0:
            c.append( a.pop(0) )
            na -= 1
        elif na == 0:
            c.append( b.pop(0) )
            nb -= 1
        elif a[0] <= b[0]:
            c.append( a.pop(0) )
            na -= 1
        else:
            c.append( b.pop(0) )
            nb -= 1
            ctr += na
    return c, ctr

def sortCount(x):
    n= len(x)
    if n == 1:
        y=x
        ctr= 0
    else:
        arrA, ctrA= sortCount(x[:n/2])
        arrB, ctrB= sortCount(x[n/2:])
        y, ctrS= mergeCount( arrA, arrB )
        ctr= ctrS + ctrA + ctrB
    return y, ctr

def naive_algorithm(testArray):
    n= len(testArray)
    ctr= 0
    for i in range(n-1):
        for j in range(i,n):
            if(testArray[i] > testArray[j]):
                ctr+=1
    return ctr


if __name__ == '__main__':
    # Initial test:
    testArray1= [5,4,3,2,1]
    print 'Naive test 1 result:', naive_algorithm(testArray1)
    print 'fast test 1 results:', sortCount(testArray1)[1]
    #
    testArray2= [19,1,3,14,2,6,23,4,7,5,8,9]
    print 'Naive test 2 result:', naive_algorithm(testArray2)
    print 'fast test 2 results:', sortCount(testArray2)[1]
    #
    #  Now us in anger
    fin= open('homework_data.txt','rb')
    hworkArray= []
    for l in fin.readlines():
        hworkArray.append ( int(l) )

    print 'Homework answer: ',sortCount( hworkArray )[1]