#!/Users/davidsutton/usr/canopy/bin/python
import sys, random, copy, gzip

class STACK:
    def __init__(self):
        self.values= []
        return None
    
    def push(self,v):
        self.values= [v] + self.values
        return None

    def pop(self):
        return self.values.pop(0)

    def reverse(self):
        self.values.reverse()
        return None

    def isempty(self):
        return len(self.values) == 0

class ENTITY():
    def __init__(self):
        self.inEntities= []
        self.outEntities= []
        self.explored= False
        return None

    def addOut(self,id):
        self.outEntities.append(id)
        return None

    def addIn(self,id):
        self.inEntities.append(id)
        return None

    def reverse(self):
        buffer= copy.deepcopy(self.outEntities)
        self.outEntities= copy.deepcopy(self.inEntities)
        self.inEntities= buffer
        return None

    def outList(self):
        return self.outEntities

class EDGE(ENTITY):
    def __init__(self,inNode,outNode):
        ENTITY.__init__(self)
        self.inEntities[inNode]= 1
        self.outEntities[outNode]= 1
        return None


class NODE(ENTITY):
    def __init__(self):
        ENTITY.__init__(self)
        self.leader= None
        self.rank= None
        return None

class DIRECTEDGRAPH():
    def __init__(self,edgeList):
        self.numEdges= 0
        self.nodeSet= {}
        for source, destination in edgeList:
            if source not in self.nodeSet:
                self.nodeSet[source]= NODE()
            self.nodeSet[source].addOut(destination)
            if destination not in self.nodeSet:
                self.nodeSet[destination]= NODE()
            self.nodeSet[destination].addIn(source)
            self.numEdges += 1
        self.numNodes= len(self.nodeSet)
        self.order= STACK()
        return None

    def reverse(self):
        for n in self.nodeSet:
            self.nodeSet[n].reverse()
            self.nodeSet[n].explored= False
        self.order.reverse()
        return self

    def show(self):
        for n,v in self.nodeSet.items():
            print n, v.inEntities, v.outEntities
        return None

def readEdgeList(fname):
    with open(fname,'rb') as f:
        edgeList= []
        for line in f:
            edgeList.append( [int(e) for e in str(line).strip().split()] )
    return edgeList

def generateEdgeList(fname):
    with gzip.open(fname,'rb') as f:
        for line in f:
            yield [int(e) for e in str(line).strip().split()]


if __name__ == '__main__':
    print 'TEST graph structure'
    print 'read graph and show'
    fname= 'testCase1.txt'
    edgeList= readEdgeList(fname)
    print edgeList[0:11]
    graph1= DIRECTEDGRAPH( readEdgeList(fname) )
    graph1.show()
    print '***reversed***'
    graph1.reverse().show()

    sys.exit()

    fname= 'testCase6.txt'
    graph= DIRECTEDGRAPH( readEdgeList(fname) )
    print graph.numNodes, graph.numEdges
    graph.reverse()
    sys.exit()