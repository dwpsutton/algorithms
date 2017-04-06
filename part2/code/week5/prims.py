'''
    Module to calculate MST of a dense city-city graph.
'''
__author__ = 'David Sutton'

import sys

class EDGE:
    def __init__(self,start,end,weight):
        self.start= start
        self.dest= end
        self.length= weight
        return None


def toEdgeList(nodes,distances):
    numNodes= len(nodes)
    numEdges= 0
    edges= []
    for a in nodes:
        for b in nodes:
            if a>b:
                edges.append( EDGE( a, b, distances[a,b]) )
                numEdges += 1
    return numNodes, numEdges, edges

def prims(nodes,distances):
    '''
        Double check that this solution is O(mn)
    '''
#    print nodes
    if len(nodes)==1:
        return 0.

    numNodes, numEdges, edges= toEdgeList(nodes,distances)

#    for edge in edges:
#        print edge.start, edge.dest

    cost= 0
    explored= {}
    explored[edges[0].start]= 0
    while len(explored) < numNodes:
        mymin= []
#        if len(explored) == 3:
#            print len(explored),explored,numNodes
#            sys.exit(-1)
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
                    if mychoice==0: print 'problem',ctr
                elif e.length < mymin:
                    mymin= e.length
                    mychoice= -ctr
                    if mychoice==0: print 'problem',ctr
        if mychoice >= 0:
            explored[edges[mychoice].dest]= 0
        else:
            explored[edges[abs(mychoice)].start]= 0
        cost += edges[abs(mychoice)].length
#        print 'kk',edges[mychoice].dest,mychoice
#    print 'bing',cost
    return cost
