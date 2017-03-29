#!/Users/davidsutton/usr/canopy/bin/python

def merge(a,b):
    na= len(a)
    nb= len(b)
    c= []
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
    return c

def sort(x):
    n= len(x)
    if n == 1:
        y=x
    else:
        y= merge( sort(x[:n/2]), sort(x[n/2:]) )
    return y

if __name__ == "__main__":
    import numpy as np
    n= 5000
    x= list(np.random.rand(n))
    y= sort(x)

    ctr=0
    for a in y:
        if ctr < n-1:
            if a > y[ctr+1]:
                print 'problem'
        ctr += 1