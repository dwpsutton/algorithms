#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np

class EDGE:
    def __init__(self,start,end,weight):
        self.start= start
        self.dest= end
        self.length= weight
        return None


def readData(fname):
    f= open(fname,'rb')
    header= f.readline().split()
    numNodes= int(header[0])
    numEdges= int(header[1])
    edges= []
    for line in f.readlines():
        this= line.split()
        edges.append( EDGE( int(this[0]), int(this[1]), float(this[2]) ) )
    f.close()
    return numNodes, numEdges, edges

if __name__ == '__main__':
    fname= 'q3_data.txt' #'prob2_testcase2.txt'
    numNodes, numEdges, edges= readData(fname)
    cost= 0
    explored= {}
    explored[edges[0].start]= 0
    while len(explored) < numNodes:
        mymin= []
        for ctr,e in enumerate(edges):
            if e.start in explored and e.dest not in explored:
                if mymin== []:
                    mymin= e.length
                    mychoice= ctr
                elif e.length < mymin:
                    mymin= e.length
                    mychoice= ctr
            elif e.dest in explored and e.start not in explored:
                if mymin== []:
                    mymin= e.length
                    mychoice= -ctr
                elif e.length < mymin:
                    mymin= e.length
                    mychoice= -ctr
        if mychoice >= 0:
            explored[edges[mychoice].dest]= 0
        else:
            explored[edges[abs(mychoice)].start]= 0
        cost += edges[abs(mychoice)].length
    print cost