#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np

def readData(fname):
    f= open(fname,'rb')
    numJobs= int(f.readline())
    weights= []
    lengths= []
    for line in f.readlines():
        weights.append( int( line.split()[0] ) )
        lengths.append( int( line.split()[1] ) )
    f.close()
    return numJobs, weights, lengths


if __name__ == '__main__':
    fname= 'q1_data.txt'
    numJobs, weights, lengths= readData(fname)

    # Difference algorithm
    benefit= map(lambda x: x[0]*1.000001 - x[1], zip(weights,lengths))
    ordering= np.argsort(benefit)
    mySum= 0
    completionTime= 0
    for i in reversed(ordering):
        completionTime += lengths[i]
        mySum += weights[i] * completionTime
    print 'difference: ',mySum

    # Ratio algorithm
    benefit=map(lambda x: x[0]/float(x[1]), zip(weights,lengths))
    ordering= np.argsort(benefit)
    mySum= 0
    completionTime= 0
    for i in reversed(ordering):
        completionTime += lengths[i]
        mySum += weights[i] * completionTime
    print 'ratio: ',mySum
