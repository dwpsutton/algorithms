#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np, copy



class graph:
    def __init__(self):
        self.edges= {}
        self.unexplored_nodes= {}
        self.explored_nodes= {}
        self.n= 0
        self.m= 0
        self.sumLength= 0
        return None

    def addEdge(self,node,tup):
        self.m += 1
        self.edges[self.m]= [node,tup[0],tup[1]] # outnode, innode, length
        self.sumLength += tup[1]
        return None

    def addNode(self,edges):
        self.n += 1
        self.unexplored_nodes[self.n]= []
        for e in edges:
            self.unexplored_nodes[self.n]= -1
            self.addEdge(self.n, e)
        return None

    def exploreNode(self,node,distance):
        self.explored_nodes[node]= distance
        del self.unexplored_nodes[node]
        return None

    def chooseUpdateEdge(self):
        choice= -1
        choiceLength= self.sumLength+1
        toCut=[]
        for e in self.edges:
            out= self.edges[e][0]
            inn= self.edges[e][1]
            length= self.edges[e][2]
            if (out in self.explored_nodes):
                if inn not in self.unexplored_nodes:
                    toCut.append( e )
                else:
                    length= length + self.explored_nodes[out]
                    #print e,out,inn,length,out in self.explored_nodes,inn not in self.unexplored_nodes
                    if length < choiceLength:
                        choice= e
                        choiceLength= length
        #for x in toCut:
        #    del self.edges[x]
        return choice


def dijkstra(graph,source,destination):
    distance= 0
    node= source
    graph.exploreNode(source,0)
    while node != destination:
        edge= graph.chooseUpdateEdge()
        thisEdge= graph.edges[edge]
        node= thisEdge[1]
        #print 'CHOICE ',distance,thisEdge[0],node,thisEdge[2]
        distance= graph.explored_nodes[thisEdge[0]] + thisEdge[2]
        graph.exploreNode(node,distance)
    
    return distance


def readData(fname):
    outt= []
    with open(fname,'rb') as f:
        for line in f:
            outt.append( [] )
            raw= line.strip().split('\t')
            for e in raw[1:]:
                tup= [int(x) for x in e.strip().split(',')]
                outt[-1].append( tup )
    return outt

if __name__ == '__main__':
    #    fname= 'testCase1.txt' #'homeworkData.txt'
    #    GRAPH= graph()
    #    nodeList= readData(fname)
    #    for n in nodeList:
    #        GRAPH.addNode(n)
            #            #
            #    for i in range(8):
        #        GRAPHI= copy.deepcopy(GRAPH)
        #        print 1,i+1,dijkstra(GRAPHI,1,i+1)


    fname2= 'homeworkData.txt'
    GRAPH2= graph()
    nodeList= readData(fname2)
    for n in nodeList:
        GRAPH2.addNode(n)
    print 'DD',GRAPH2.sumLength,len(nodeList)

    destinations= [7,37,59,82,99,115,133,165,188,197]
    distances= ''
    for j in destinations:
        GRAPHJ= copy.deepcopy(GRAPH2)
        distances += str(dijkstra(GRAPHJ, 1, j))+str(',')
print distances[:-1]