#!/Users/davidsutton/usr/canopy/bin/python
from datetime import datetime, timedelta

def readData(filename):
    f= open(filename,'rb')
    out= []
    for x in f:
        out.append( int(x) )
    return out

def lookupTable(array):
    haveSeen= {}
    for x in array:
        haveSeen[x]= 1
    return haveSeen

def numDistinctPairs(array,haveSeen,target):
    num= 0
    for x in array:
        partner= target - x
        if partner in haveSeen:
            if partner != x:
                num += 1
    return num



if __name__ == "__main__":
    filename= "homework_data_2sum.txt"
    data= readData(filename)
    haveSeen= lookupTable(data)
    tc= datetime.now()
    ctr= 0
    for i in range(-10000,10001):
        if numDistinctPairs(data,haveSeen,i) > 0:
            ctr+=1
    print (datetime.now() - tc).total_seconds() / len(range(-10000,10001))
    print ctr

    #answer= 427