#!/Users/davidsutton/usr/canopy/bin/python
from datetime import datetime, timedelta
import copy,sys




class HEAP:
    def __init__(self,kind=0):
        if kind==0:
            self._amMinHeap= True
            self._amMaxHeap= False
        elif kind==1:
            self._amMaxHeap= True
            self._amMinHeap= False
        else:
            print 'Invalide heap type specified!'
            sys.exit(-1)
        self._array_= []
        self.len= 0
        return None

    def insert(self,x):
        self._array_.append(x)
        self.len += 1
        i= self.len
        while i > 1:
            j= self._getParent(i)
            if self._amMinHeap and ( self._array_[i-1] >= self._array_[j-1] ):
                break
            elif self._amMaxHeap and ( self._array_[i-1] <= self._array_[j-1] ):
                break
            parent= copy.deepcopy(self._array_[j-1])
            self._array_[j-1]= copy.deepcopy(self._array_[i-1])
            self._array_[i-1]= parent
            i = j
        return None

    def extractRoot(self):
        minimum= copy.deepcopy(self.root())
        i= 1
        if self.len > 1:
            self._array_[0]= self._array_.pop(-1)
            self.len -= 1
        else:
            self._array_.pop(-1)
            self.len=0
        
        while self.len > 1:
            children= self._getChildren(i)
            if children[0] > self.len:
                break
            elif children[1] > self.len:
                j= children[0]
            elif self._amMinHeap and  self._array_[children[0]-1] < self._array_[children[1]-1]:
                j=children[0]
            elif self._amMaxHeap and self._array_[children[0]-1] > self._array_[children[1]-1]:
                j= children[0]
            else:
                j= children[1]
            if self._amMinHeap and self._array_[i-1] <= self._array_[j-1]:
                break
            elif self._amMaxHeap and self._array_[i-1] >= self._array_[j-1]:
                break
            else:
                parent= copy.deepcopy( self._array_[i-1] )
                self._array_[i-1]= copy.deepcopy( self._array_[j-1] )
                self._array_[j-1]= parent
            i=j
        return minimum

    def root(self):
        if self.len > 0:
            return self._array_[0]
        else:
            return None

    def _getParent(self,i):
        return i/2
    
    def _getChildren(self,i):
        return [2*i, 2*i+1]


def feedData(filename):
    f= open(filename,'rb')
    while True:
        x= f.readline()
        if not x:
            break
        yield int( x )

def testHeap(filename):
    minHeap= HEAP() # This is a minHeap by default
    #
    # First check insertion
    print 'Testing insertion'
    amOK= True
    for x in feedData(filename):
        minHeap.insert(x)
        l= minHeap.len
        if minHeap.root() != min(minHeap._array_):
            amOK= False
            print 'uh oh!',minHeap.root(), min(minHeap._array_), minHeap._array_[0:3]
    print 'passed=',amOK
    #
    # Now check extractMin
    mememe= sorted(minHeap._array_)
    checker= []
    for i in range(10000):
        checker.append( minHeap.extractRoot() )
    print 'Testing extractMin'
    print 'passed=',checker == mememe[:10000]
    #
    # OK seems to work :)
    return None




if __name__ == '__main__':
    filename= 'homeworkData_Median.txt'
    #testHeap(filename)
    #sys.exit(-1)

    medianSum= 0

    minHeap= HEAP(kind=0)
    maxHeap= HEAP(kind=1)
    for x in feedData(filename):
        if x > minHeap.root():
            minHeap.insert(x)
        else:
            maxHeap.insert(x)
        if maxHeap.len >=1 or minHeap.len >= 1:
            #Rebalance if necessary
            if maxHeap.len > minHeap.len:
                minHeap.insert( maxHeap.extractRoot() )
            if minHeap.len > maxHeap.len + 1:
                maxHeap.insert( minHeap.extractRoot() )
            
            #Print online median
            if maxHeap.len == minHeap.len-1:
                imedian= minHeap.root()
            elif minHeap.len == maxHeap.len:
                imedian= maxHeap.root()
            else:
                print 'Uh oh, unbalanced!'
            medianSum += imedian
    print medianSum%10000
    #1213




