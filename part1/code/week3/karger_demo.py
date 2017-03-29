#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np, sys, random, copy

class nodeClass():
    def __init__(self,id,nodeList):
        self._id= id
        self._edges= {}
        for n in nodeList:
            self._edges[n]= 1 #Contains the number of links
        return None

    def updateEdges(self, replaceThis, withThis ):
        if replaceThis in self._edges:
            if withThis in self._edges:
                self._edges[withThis] += self._edges.pop(replaceThis)
            else:
                self._edges[withThis] = self._edges.pop(replaceThis)
        else:
            print 'Expected edge missing from graph in updateEdges: exiting!'
            sys.exit(-1)
        return None

    def mergeEdgeInfo(self,nodeDict):
        for id in nodeDict:
            if id in self._edges:
                self._edges[id] += nodeDict[id]
            else:
                self._edges[id] = nodeDict[id]
        return None

    def cutSelfLoops(self):
        if self._id in self._edges:
            del self._edges[self._id]
        return None

    def getEdges(self):
        return self._edges


def mergeNodes( graph, idOld, idNew):
    
    # Get the node to be merged in (pop removes it from graph)
    nodeOld= graph.pop(idOld)
    
    # Update third party nodes (starting points of edges)
    for id in nodeOld.getEdges():
        if id in graph:
            graph[id].updateEdges(idOld,idNew)
        else:
            print 'Expected third party node is missing in merge!'
            sys.exit(-1)

    # Merge the nodeDicts
    graph[ idNew ].mergeEdgeInfo( nodeOld.getEdges() )

    # Remove self loops
    graph[ idNew ].cutSelfLoops()

    return graph


def sampleEdge(graph):
    edges= []
    for n in graph:
        nodesEdges= graph[n].getEdges()
        for e in nodesEdges:
            for i in range( nodesEdges[e] ):
                # add as many times as the count in the nodeClass
                edges.append( (n, e) )
    choice= random.choice(edges)
    return choice


def randomContractGraph(graph):
    n= len(graph)
    while n > 2:
        choice= sampleEdge(graph)
        graph= mergeNodes( graph, choice[0], choice[1] )
        n -= 1
    return graph


def kargerContraction(graph,seed=1):
    random.seed(seed)
    n= len(graph)
    minCount= n
    outgraph= copy.deepcopy(graph)
    for i in range(n): #range(int((n/4.)**2 * np.log(n/4.)) ): #nb: the suggested number in lectures takes too long and is overkill for the simple graphs in the tests and homework.
        g2= randomContractGraph(copy.deepcopy(graph))
        count= g2[ g2.keys()[0] ].getEdges().values()[0]
        if count < minCount:
            minCount= count
            outgraph= g2
    return minCount, outgraph


def readGraph(fileHandle):
    graph= {}
    for line in fileHandle:
        elements= line.split()
        id= int(elements[0])
        nodeList= map(int,elements[1:])
        if id in graph:
            print 'problem reading graph: node is repeated!'
            sys.exit(-1)
        graph[id]= nodeClass(id,nodeList)
    return graph

def printGraph(graph):
    for n in graph:
        print graph[n]._id
        print ' ',graph[n].getEdges()


if __name__ == '__main__':
    graph= readGraph(open('homework_data.txt','rb'))
    for i in range(2):
        n, gg= kargerContraction(graph,seed=i)
        print n, sampleEdge(gg)